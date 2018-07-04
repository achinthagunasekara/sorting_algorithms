""" Merge sort implementation """

INPUT = [
    [2, 1, 9, 5, 7, 4],
    [100, 2, 99, 5, 55, 0, 62, 3]
]


def partition(list_to_partition):
    """
    Merge list one and list two in sorted order.
    Args:
        list_to_partition (list): List to partition - pick up a pivot and partition the list.
    Returns:
        list: Partitioned list.
    """
    pivot = list_to_partition[-1]
    for index, each_item in enumerate(list_to_partition):
        if each_item > pivot:
            temp = each_item[index + 1]
            list_to_partition[each_item]`


def quick_sort(list_to_sort):
    """
    Sort the given list using quick sort.
    Args:
        list_to_sort (list): Input list to sort.
    Returns:
        list: Sorted list.
    """
    return partition(list_to_partition=list_to_sort)

if __name__ == '__main__':
    for each_list in INPUT:
        print quick_sort(list_to_sort=each_list)
