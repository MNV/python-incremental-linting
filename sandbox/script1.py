def merge_sort(array):
    array_len = len(array)
    if array_len < 2:
        return array

    mid = array_len // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            right = right[1:]
    if left:
        merged += left
    if right:
        merged += right

    return merged


if __name__ == "__main__":
    print(merge_sort([4, 2, 7, 8, 9, 0, 54, 3, 2, 3, -12, 2, 0, 5, 1, 1, 2]))
