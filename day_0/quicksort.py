import sys


def q_sort(array):
    """
    In-place quick sort implementation with one pivot and
    Hoare partition scheme.
    """
    q_sort_util(array, 0, len(array) - 1)


def q_sort_util(array, i_b, i_e):
    if i_b < i_e:
        pivot = q_sort_part(array, i_b, i_e)
        q_sort_util(array, i_b, pivot - 1)
        q_sort_util(array, pivot + 1, i_e)
    return array


def q_sort_part(array, i_b, i_e):
    pivot = array[i_e]
    i = i_b
    for j in xrange(i_b, i_e):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[i_e] = array[i_e], array[i]
    return i


def test():
    import random
    for _ in xrange(100):
        size = random.randint(0, 100000)
        array = range(size)
        array_copy = array[:]
        random.shuffle(array_copy)
        q_sort(array_copy)
        print array == array_copy, size
    return 0


if __name__ == "__main__":
    sys.exit(test())
