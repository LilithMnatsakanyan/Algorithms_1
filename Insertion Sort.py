# 1
def insertionsort(l):
    n = len(l)
    if n <= 1:
        return l
    for i in range(1, n):
        for j in range(0, i):
            while (j>=0 and l[i]< l[j]):
                l[i], l[j] = l[j], l[i]
    return l



l = [1, 0, 10, 5, 6, 1]
print(insertionsort(l))

# 2

def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



arr = [-9, 12, 23, 0, 99]
insertionSort(arr)
print(arr)

