def merge_sort(arr):
    """
    对数组 arr 进行归并排序。
    """
    if len(arr) <= 1:
        return arr

    # 分割数组
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 合并已排序的两半
    return merge(left_half, right_half)

def merge(left, right):
    """
    合并两个已排序的列表 left 和 right。
    """
    sorted_list = []
    left_index, right_index = 0, 0

    # 比较并合并两个列表
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # 如果左边或右边还有剩余的元素，将它们添加到结果列表中
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list

# 示例数组
sample_array = [34, 7, 23, 32, 5, 62]
sorted_array = merge_sort(sample_array)
print("Sorted array:", sorted_array)
