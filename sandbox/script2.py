from typing import Optional
from random import choice


def quicksort(array: list) -> list:
    if len(array) < 2:
        return array

    pivot_index = choice(range(len(array)))
    pivot = array[pivot_index]

    excluded_array = array[:pivot_index] + array[pivot_index + 1 :]

    left = [v for v in excluded_array if v <= pivot]
    right = [v for v in excluded_array if v > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


def binary_search(array: list, value: int) -> Optional[int]:
    low_indx = 0
    high_indx = len(array) - 1

    while low_indx <= high_indx:
        mid_indx = (low_indx + high_indx) // 2
        guess = array[mid_indx]
        if guess == value:
            return mid_indx

        if guess < value:
            low_indx = mid_indx + 1
        else:
            high_indx = mid_indx - 1

    return None


if __name__ == "__main__":
    l = [2, 40, 35, 50, 1, 0, 50, 67, 0, -40, 23]
    l_sorted = quicksort(l)
    print(l_sorted)

    search = 50
    print(binary_search(l_sorted, search))
