"""Functions that implement sorting algorithms."""
__author__ = "730469865"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    sorted_idx = 0
    while sorted_idx < len(x) - 1:
        unsorted_idx = sorted_idx + 1 
        while unsorted_idx > 0 and x[unsorted_idx] < x[unsorted_idx - 1]:
            swapping_num = x[unsorted_idx]
            x[unsorted_idx] = x[unsorted_idx - 1]
            x[unsorted_idx - 1] = swapping_num
            unsorted_idx -= 1
        sorted_idx += 1 
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    idx: int = 0
    while idx < len(x):
        min_idx = idx
        idx2 = min_idx
        while idx2 < len(x) - 1:
            if x[idx2 + 1] < x[min_idx]:
                min_idx = idx2 + 1
            idx2 += 1
        swapping_num = x[idx]
        x[idx] = x[min_idx]
        x[min_idx] = swapping_num
        idx += 1
    return None
    