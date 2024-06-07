def has_contiguous_subarray_with_sum(arr, target):
    start = 0
    current_sum = 0
    
    for end in range(len(arr)):
        current_sum += arr[end]
        
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1
        
        if current_sum == target:
            return True
    
    return False

arr = [4, 2, 7, 1, 9, 5, 6]
target = 17
print(has_contiguous_subarray_with_sum(arr, target))