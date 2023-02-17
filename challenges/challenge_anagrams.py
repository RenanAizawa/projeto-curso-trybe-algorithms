# https://www.geeksforgeeks.org/python-program-for-selection-sort/


def selectionSort(list_to_sort, size):
    for i in range(size):
        min_index = i

        for n in range(i + 1, size):
            if list_to_sort[n] < list_to_sort[min_index]:
                min_index = n
        (
            list_to_sort[i], list_to_sort[min_index]) = (
                list_to_sort[min_index], list_to_sort[i])
    return list_to_sort


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    list1 = list(first_string.lower())
    list2 = list(second_string.lower())
    sorted1 = selectionSort( list1, len(list1))
    sorted2 = selectionSort( list2, len(list2))
    merged1 = "".join(sorted1)
    merged2 = "".join(sorted2)
    if not first_string or not second_string:
        return (merged1, merged2, False)
    return (merged1, merged2, merged1 == merged2)
