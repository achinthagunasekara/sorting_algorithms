""" Quick sort implementation """


def partition(list_to_partition):
    """
    Merge list one and list two in sorted order.
    Args:
        list_to_partition (list): List to partition - pick up a pivot and partition the list.
    Returns:
        list: Partitioned list.
    """
    pivot = list_to_partition[-1]
    partition_index = 0
    # Swap all items less then pivot to the left of the partition index
    for index in range(0, len(list_to_partition)):
        if index < len(list_to_partition) - 1 and list_to_partition[index] <= pivot:
            tmp = list_to_partition[index]
            list_to_partition[index] = list_to_partition[partition_index]
            list_to_partition[partition_index] = tmp
            partition_index += 1
    # Finally swap the partition index with the pivot
    tmp = list_to_partition[partition_index]
    list_to_partition[partition_index] = list_to_partition[-1]
    list_to_partition[-1] = tmp
    return list_to_partition


def quick_sort(list_to_sort):
    """
    Sort the given list using quick sort.
    Args:
        list_to_sort (list): Input list to sort.
    Returns:
        list: Sorted list.
    """
    return partition(list_to_partition=list_to_sort)


INPUT = [
    [2, 1, 9, 5, 7, 4],
    [100, 2, 99, 5, 55, 0, 62, 3]
]


if __name__ == '__main__':
    for each_list in INPUT:
        print quick_sort(list_to_sort=each_list)
