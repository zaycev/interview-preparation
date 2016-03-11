import sys


def bin_search(array, key):
    """
    Classic, non-recursive implementation of binary search.
    """
    return bin_search_util(array, key, 0, len(array) - 1)


def bin_search_util(array, key, i_b, i_e):
    while True:
        mid = i_b + (i_e - i_b) // 2
        if array[mid] == key:
            return mid
        if mid == i_b and mid == i_e:
            raise KeyError("Key %r not found." % key)
        if array[mid] > key:
            i_e = mid - 1
        else:
            i_b = mid + 1


def test():
    import random
    import quicksort
    import mergesort
    for _ in xrange(100):
        array = list(set([random.randint(0, 1000000) for r in xrange(10000)]))
        quicksort.q_sort(array)
        key_i = random.randint(0, len(array) - 1)
        key = array[key_i]
        print len(array), key == array[bin_search(array, key)]
    return 0


if __name__ == "__main__":
    sys.exit(test())
