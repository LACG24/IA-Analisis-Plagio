def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def adaptive_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        return arr
    mid = len(arr) // 2
    left = adaptive_merge_sort(arr[:mid])
    right = adaptive_merge_sort(arr[mid:])
    return merge(left, right)
