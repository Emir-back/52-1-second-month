def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return f"Элемент {target} найден на индексе {mid}."
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return f"Элемент {target} не найден в списке."


arr = [64, 34, 25, 12, 22, 11, 90]

sorted_arr = bubble_sort(arr)
print(f"Отсортированный список: {sorted_arr}")

target = 22
result = binary_search(sorted_arr, target)
print(result)
