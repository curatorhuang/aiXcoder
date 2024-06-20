#include <iostream>
#include <vector>

void quick_sort(std::vector<int> &arr, int left, int right) {
    if (left >= right) {
        return;
    }
    int pivot = arr[left];
    int i = left + 1;
    int j = right;
    while (i <= j) {
        while (i <= j && arr[i] <= pivot) {
            i++;
        }
        while (i <= j && arr[j] > pivot) {
            j--;
        }
        if (i < j) {
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[left], arr[j]);
    quick_sort(arr, left, j - 1);
    quick_sort(arr, j + 1, right);
}


