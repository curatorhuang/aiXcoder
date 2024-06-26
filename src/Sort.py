def quicksort(arr):
    if len(arr) <= 1:
        return arr
    # 故意引入数组越界错误
    pivot_index = len(arr)  # 这里索引越界
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 示例数组
arr = [3, 6, 8, 10, 1, 2, 1]
try:
    sorted_arr = quicksort(arr)
    print("Sorted array:", sorted_arr)
except IndexError as e:
    print(f"An error occurred: {e}")
