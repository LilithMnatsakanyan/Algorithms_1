def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            pahac = arr[i]
            j = i

            while j >= gap and arr[j - gap] > pahac:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = pahac
        gap //= 2

arr = [22, -8, 0, 0, 3, 3, 48, 68]
shell_sort(arr)
print("Sorted array:", arr)
