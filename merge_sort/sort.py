""" Merge sort implementation """

INPUT = [
    [2, 1, 9, 5, 7, 4],
    [100, 2, 99, 5, 55, 0, 62, 3]
]


def merge(list_one, list_two, orginal_list):
    """
    Merge list one and list two in sorted order.
    Args:
        list_one (list): Sorted sub list.
        list_two (list): Sorted sub list.
        orgial_list (list): Orginal unsorted list.
    Returns:
        list: sorted orginal list.
    """
    list_one_index = 0
    list_two_index = 0
    original_list_index = 0
    while list_one_index < len(list_one) and list_two_index < len(list_two):
        if list_one[list_one_index] < list_two[list_two_index]:
            orginal_list[original_list_index] = list_one[list_one_index]
            list_one_index += 1
        else:
            orginal_list[original_list_index] = list_two[list_two_index]
            list_two_index += 1
        original_list_index += 1
    while list_one_index < len(list_one):
        orginal_list[original_list_index] = list_one[list_one_index]
        list_one_index += 1
        original_list_index += 1
    while list_two_index < len(list_two):
        orginal_list[original_list_index] = list_two[list_two_index]
        list_two_index += 1
        original_list_index += 1
    return orginal_list


def merge_sort(list_to_sort):
    """
    Sort the given list using merge sort.
    Args:
        list_to_sort (list): Input list to sort.
    Returns:
        list: Sorted list.
    """
    if not len(list_to_sort) > 1:
        return None
    middle_index = len(list_to_sort)/2
    list_one = list_to_sort[0:middle_index]
    list_two = list_to_sort[middle_index:]
    merge_sort(list_to_sort=list_one)
    merge_sort(list_to_sort=list_two)
    merge(list_one=list_one, list_two=list_two, orginal_list=list_to_sort)
    return list_to_sort


if __name__ == '__main__':
    for each_list in INPUT:
        print merge_sort(each_list)
