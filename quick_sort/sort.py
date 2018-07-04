""" Quick sort implementation """


def partition(list_to_partition, from_index, to_index):
    """
    Merge list one and list two in sorted order.
    Args:
        list_to_partition (list): List to partition - pick up a pivot and partition the list.
    Returns:
        list: Partitioned list.
    """
    pivot = list_to_partition[to_index]
    partition_index = from_index
    # Swap all items less then pivot to the left of the partition index
    for index in range(from_index, to_index):
        if list_to_partition[index] <= pivot:
            tmp = list_to_partition[index]
            list_to_partition[index] = list_to_partition[partition_index]
            list_to_partition[partition_index] = tmp
            partition_index += 1
    # Finally swap the partition index with the pivot
    tmp = list_to_partition[partition_index]
    list_to_partition[partition_index] = list_to_partition[to_index]
    list_to_partition[to_index] = tmp
    return partition_index


def quick_sort(list_to_sort, from_index=None, to_index=None):
    """
    Sort the given list using quick sort.
    Args:
        list_to_sort (list): Input list to sort.
    Returns:
        list: Sorted list.
    """
    if from_index is None:
        from_index = 0

    if to_index is None:
        to_index = len(list_to_sort) - 1

    if  from_index < to_index:
        partition_index = partition(list_to_partition=list_to_sort,
                                    from_index=from_index,
                                    to_index=to_index)
        # Sort the left segment from the pivot
        quick_sort(list_to_sort=list_to_sort,
                   from_index=from_index,
                   to_index=partition_index - 1)
        # Sort the right segment from the pivot
        quick_sort(list_to_sort=list_to_sort,
                   from_index=partition_index + 1,
                   to_index=len(list_to_sort) - 1)
    return list_to_sort


INPUT = [
    [2, 1, 9, 5, 7, 4],
    [100, 2, 99, 5, 55, 0, 62, 3],
    [1233, 223, 4, 55, 21, 56, 33, 4],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 1, 1, 3, 3, 3, 2, 2]
]


if __name__ == '__main__':
    for each_list in INPUT:
        print quick_sort(list_to_sort=each_list)
