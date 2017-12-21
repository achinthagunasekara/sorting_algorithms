""" Implementation of selection sort algorithm """

def selection_sort(list_to_sort):
    """
    Sort a list using selection sort algorithm
    Args:
        list_to_sort (list): Unsorted list to sort.
    Returns:
        list: Sorted list.
    """
    for outter_index, outter_element in enumerate(list_to_sort):  # pylint: disable=unused-variable
        smallest_index = outter_index
        for inner_index in range(outter_index, len(list_to_sort)):
            if list_to_sort[inner_index] < list_to_sort[smallest_index]:
                smallest_index = inner_index
        list_to_sort[outter_index], list_to_sort[smallest_index] = \
            list_to_sort[smallest_index], list_to_sort[outter_index]
    return list_to_sort


TO_SORT = [
    [1, 9, -5, 12, 2, 3, 4, 20, 6],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [10, -5, -4, 9, 9, 4, 9, 7]
]

for each_list in TO_SORT:
    print selection_sort(each_list)
