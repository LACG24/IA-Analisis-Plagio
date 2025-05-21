def shell_sort_hibbard(arr):
    n = len(arr)
    gaps = []
    k = 1
    while (gap := 2**k - 1) < n:
        gaps.insert(0, gap)
        k += 1

    for gap in gaps:
        for i in range(gap, n):
            actual = arr[i]
            j = i
            while j >= gap and arr[j - gap] > actual:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = actual
    return arr
