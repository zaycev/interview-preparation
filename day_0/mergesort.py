import sys


def merge_sort(array):
    """
    In-place, top-down implementation using temporary buffer for merging.
    """
    if len(array) < 2:
        return
    temp = [0] * len(array)
    merge_sort_util(array, temp, 0, len(array) - 1)
    return array


def merge_sort_util(array, temp, i_b, i_e):
    """
    Sort partition of array using temporary buffer for merging.
    """

    # Handle ordinary cases.
    if i_e == i_b:
        return
    elif i_e - i_b == 1:
        if array[i_b] > array[i_e]:
            array[i_b], array[i_e] = array[i_e], array[i_b]
        return
    
    # Partition array using mid index.
    mid = i_b + (i_e - i_b) / 2

    # Sort partitions.
    merge_sort_util(array, temp, i_b, mid)
    merge_sort_util(array, temp, mid, i_e)
    
    i, j, k = i_b, mid, 0

    # Merge sorted arrays using temp array.
    while (i < mid) and (j < i_e + 1):
        if array[i] < array[j]:
            temp[k] = array[i]
            i += 1
        else:
            temp[k] = array[j]
            j += 1
        k += 1

    # Copy remaining items to temp.
    while i < mid:
        temp[k] = array[i]
        i += 1
        k += 1
    while j < i_e + 1:
        temp[k] = array[j]
        j += 1
        k += 1

    # Copy sorted items from temp to array.
    for i in xrange(i_e - i_b + 1):
        array[i_b + i] = temp[i]


def test():
    import random
    for _ in xrange(100):
        size = random.randint(0, 10000)
        array = range(size)
        array_copy = array[:]
        random.shuffle(array_copy)
        merge_sort(array_copy)
        print array == array_copy, size
    return 0

if __name__ == '__main__':
    sys.exit(test())


