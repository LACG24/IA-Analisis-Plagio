def flash_sort(arr):
    n = len(arr)
    if n == 0:
        return arr

    m = int(0.45 * n)
    max_idx = 0
    min_val = arr[0]
    for i in range(1, n):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > arr[max_idx]:
            max_idx = i

    if arr[max_idx] == min_val:
        return arr

    L = [0] * m
    c = (m - 1) / (arr[max_idx] - min_val)
    for i in range(n):
        k = int(c * (arr[i] - min_val))
        L[k] += 1

    for i in range(1, m):
        L[i] += L[i - 1]

    arr[0], arr[max_idx] = arr[max_idx], arr[0]
    move = 0
    j = 0
    k = m - 1
    while move < n - 1:
        while j > L[k] - 1:
            j += 1
            k = int(c * (arr[j] - min_val))
        evicted = arr[j]
        while j != L[k]:
            k = int(c * (evicted - min_val))
            dest = L[k] - 1
            arr[dest], evicted = evicted, arr[dest]
            L[k] -= 1
            move += 1

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
