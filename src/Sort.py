def quicksort(arr):
    if len(arr) <= 1：
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

# 测试
arr = [5, 2, 8, 3, 1, 6, 4]
print(quicksort(arr))  # [1, 2, 3, 4, 5, 6, 8]

