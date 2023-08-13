def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Exmaple usage
sorted_array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_value = 12
result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Target value {target_value} found at index {result}.")
else:
    print("Target value not found in the array.")