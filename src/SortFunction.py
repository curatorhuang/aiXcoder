def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

#
arr = [3, 6, 8, 10, 1, 2, 1]
try:
    sorted_arr = quicksort(arr)
    print("Sorted array:", sorted_arr)
except IndexError as e:
    print(f"An error occurred: {e}")
