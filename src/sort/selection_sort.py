"""Selection Sort Algorithm"""


def selection_sort(arr: list) -> list:
    """Sorts a given list using selection sort algorithm

    Examples:
        >>> selection_sort([8,9, 6, 7, 4, 5, 1, 3, 2])
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Args:
        arr (list): list to be sorted

    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
