def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_arr = []
    while left and right:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))

    sorted_arr.extend(left or right)
    return sorted_arr


arr = [64, 25, 12, 22, 11]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

