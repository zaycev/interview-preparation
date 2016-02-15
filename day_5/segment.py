import math
import sys
import collections

class Segmentizer():
    """
    Brute Force word segmentizer. 
    """

    def __init__(self, unigrams_path, bigrams_path):

        self.unigrams = collections.Counter()
        self.bigrams = collections.Counter()
        self.u_denom = 0.0
        self.b_denom = 0.0

        # Read unigrams
        with open(unigrams_path, "r") as unigrams:
            for line in unigrams:
                word, count = line.strip("\n").split("\t")
                count = float(count)
                self.unigrams[word] = math.log10(count)
                self.u_denom += count
        self.u_denom = math.log10(self.u_denom)

        # Read bigrams
        with open(bigrams_path, "r") as bigrams:
            for line in bigrams:
                word, count = line.strip("\n").split("\t")
                count = float(count)
                self.bigrams[word] = math.log10(count)
                self.b_denom += count
        self.b_denom = math.log10(self.b_denom)

    def segmentize(self, string, k_best=3):
        candidates = []
        self.__segm_util(string, [], candidates)
        candidates = [(self.score(c), c) for c in candidates]
        candidates = [(s, c) for s, c in candidates if s > 0]
        return list(reversed(sorted(candidates)))[:k_best]

    def score(self, candidate):
        score = 0.0
        if len(candidate) == 0:
            score = self.unigrams[candidate[0]]
        else:
            prev = candidate[0]
            for i in xrange(1, len(candidate)):
                word = candidate[i]
                bigram = "% %" % (prev, word)
                if bigram not in self.bigrams:
                    score = score - self.unigrams[w] - self.u_denom
                else:
                    score = score + self.bigrams[bigram] - self.b_denom
                prev = w
        return 10 ** score

    def __segm_util(self, string, candidate, candidates):
        if len(string) == 0 and len(candidate) > 0:
            candidates.append(candidate[:])
            return
        for i in xrange(1, len(string) + 1):
            w = string[:i]
            if w in self.unigrams:
                candidate.append(w)
                self.__segm_util(string[i:], candidate, candidates)
                candidate.pop(len(candidate) - 1)

def test():
    segm = Segmentizer("./data/unigrams.txt", "./data/bigrams.txt")
    print segm.segmentize("louisanddanielle")
    print segm.segmentize("thewalkingdead")
    print segm.segmentize("johnwall")
    print segm.segmentize("markzuckerberg")
    print segm.segmentize("fuckcancer")
    print segm.segmentize("fightlikeagirl")
    print segm.segmentize("opensource")
    return 0

if __name__ == "__main__":
    sys.exit(test())
