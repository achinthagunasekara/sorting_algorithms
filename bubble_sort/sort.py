""" Bubble sort implementation """

def bubble_sort(list_to_sort):
    """
    Sort a list using bubble sort.
    Args:
        list_to_sort (list): Unsorted list to sort.
    Returns:
        list: Sorted list.
    """
    for _ in list_to_sort:
        for i, element in enumerate(list_to_sort):
            if i < len(list_to_sort) - 1 and element > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], element
    return list_to_sort

TO_SORT = [
    [1, 9, -5, 12, 2, 3, 4, 20, 6],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [10, -5, -4, 9, 9, 4, 9, 7]
]

for each_list in TO_SORT:
    print bubble_sort(each_list)
