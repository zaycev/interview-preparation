"""
Counts number of distinct strings in the input stream (set cardinality).

Usage:
    >> python hll.py < strings.txt
    >> 

Requirements:

    * pyhash

"""

import datetime
import math
import pyhash
import random
import sys
import time
import numpy as np

class FMCounter(object):
    """Set cardinality estimator which uses Flajolet-Martin algorithm

    References:

    [1] MMDS. Chapter 4: http://infolab.stanford.edu/~ullman/mmds/ch4.pdf

    Summary from [1]:

        The more different elements we see in the stream, the more different
        hash-values we shall see. Whenever we apply a hash function h to a
        stream element a, the bit string h(a) will end in some number of 0's,
        possibly none. Call this number the tail length for a and h. Let R
        be the maximum tail length of any a seen so far in the stream. Then
        we shall use estimate 2^R for the number of distinct elements seen
        in the stream. To make estimation more robust we will take a median
        of averages from multiple hash-functions. 

    """

    # Possible hash functions.
    HASHERS = {
        32 : pyhash.murmur1_32,
        64 : pyhash.murmur2_x86_64b,
        128 : pyhash.murmur3_x86_128,
    }

    def __init__(self, n_hash_bins=7, n_hash_bin_size=16, hash_size=32):
        """
        Args:
            n_hash_bins: A number of hash bins. We will take a median of average
                         R in each bean.
            n_hash_bin_size: A size of each has bin. Should be ~ log_2 (number
                         of unique elements)
            hash_size: Size of hash function (number of bits it returns).
        """
        if hash_size not in self.HASHERS:
            raise ValueError("Hash size must be in %s" % str(self.HASHERS.keys()))
        self.hash_size = hash_size
        self.seeds = [None] * (n_hash_bins * n_hash_bin_size)
        self.n_hash_bins = n_hash_bins
        self.n_hash_bin_size = n_hash_bin_size
        self.bit_flags = [2**k for k in xrange(self.hash_size)]
        self.bit_flags_rev = list(reversed(self.bit_flags))
        self.hasher = self.HASHERS[hash_size]()

    def count(self, stream):
        random.seed(datetime.datetime.now())
        for i in xrange(len(self.seeds)):
            self.seeds[i] = random.randint(0, 2 ** self.hash_size - 1)
        estimates = np.zeros(len(self.seeds))
        b = self.bit_flags_rev
        for i, line in enumerate(stream):
            for j, seed in enumerate(self.seeds):
                h = self.hasher(line, seed=seed)
                r = self.__tl(h, b)
                if r > estimates[j]:
                    estimates[j] = r
        for i in xrange(len(estimates)):
            if estimates[i] > 0:
                estimates[i] -= 1
            estimates[i] = 2 ** estimates[i]
        bins = [list() for _ in xrange(self.n_hash_bins)]
        for i, r in enumerate(estimates):
            bin_i = i / self.n_hash_bin_size
            bins[bin_i].append(r)
        bin_means = []
        for bin_data in bins:
            bin_means.append(np.mean(bin_data))
        return np.median(bin_means)


    def __tl(self, n, b):
        for i, f in enumerate(b):
            if f & n:
                return i
        return len(b)

def test():

    test_input = [
        '849944012812', 'cookings',
        'ni2503190', 'choopa board',
        'little tea spock',
        'suede  jacket',
        '9781481927666',
        '9780060565565', 'ni2503190',
        '9781405156622', 'urv',
        'snowboard deck',
        'samsung galaxy edge charger',
        'wickr messaging',
        'choopa board', 'choopa board',
        'lundberg rice 25 lbs',
        'pink floyd  final cut',
        'lego birthday party supplies',
        'john stanford',
        'kershaw black clash',
        'dji phantom 3 charger',
        '9780375702303',
        'dji phantom 3 charger',
        'inflatable belly',
        'william glasser books',
        'newbo', '920-008045 logitech',
        'great americans',
        '9781481927666', 'scootee',
        'waterpens', '9780262581080',
        'lg k7  phone case',
        'portable shampoo chair',
        'curlformers dupe',
        'guess sandal', '3  prong plug',
        'william glasser books',
        'baroleum', 'jump tope',
        'ko\xe2\x80\x86se',
        'pairing chisels',
        'suede  jacket',
        'william glasser books',
        '9781481927666',
        'baby clothes calvin klein',
        'suede  jacket',
        '9780495798576',
        'kershaw black clash',
        '9780060565565', 'jump tope',
        'curlformers dupe',
        'snowboard deck',
        'boost mobile samsung galaxy s5',
        '9781481927666',
        'lottery results',
        'mary  j blage dvd',
        'lightbox photography cards',
        'great americans', 'b005hoo8q6',
        'taekwondo equipment',
        'smartphone', '9781481927666',
        'b005hoo8q6', 'zytenz for men',
        'guess sandal', 'tweetbot',
        'william glasser books',
        'the walking dead comic',
        'ys park comb',
        '920-008045 logitech',
        'half pad', 'guess sandal',
        'great americans',
        'omoji pillows',
        '3  prong plug', '849944012812',
        'quarterback p',
        'python machine learning',
        'slow cooker liners',
        'ys park comb', 'mullber',
        'great americans', 'cookings',
        'ko\xe2\x80\x86se',
        'xerox  phaser 6500',
        'leg garters', 'snowboard deck',
        'cookings',
        'xerox  phaser 6500',
        'macbook air 11  cover',
        'cream lip', '9780226751290',
        '9780262581080',
        'racecar tie clip',
        '9781481927666', 'baroleum',
        'quarterback p',
        'success through a positive mental attitude'
    ]
    test_input = test_input * 1000


    fm_counter = FMCounter(n_hash_bins=4, n_hash_bin_size=8, hash_size=32)

    print len(test_input), len(set(test_input))
    print fm_counter.count(test_input)

    return 0


if __name__ == "__main__":
    sys.exit(test())

