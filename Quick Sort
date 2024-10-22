arr = [0,9,3,8,2,7,5,5]

def quick_sort(arr):
  length = len(arr)
  if length <= 1:
    return arr
  else:
    pivot = arr.pop()

  right = []
  left = []
  for i in arr:
    if i <= pivot:
      left.append(i)
    else:
      right.append(i)
  return quick_sort(left) +[pivot]+ quick_sort(right)

print(quick_sort(arr))
