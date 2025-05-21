def radix_sort_256(arr):
    for byte in range(4):  # hasta 32 bits
        buckets = [[] for _ in range(256)]
        for num in arr:
            key = (num >> (byte * 8)) & 0xFF
            buckets[key].append(num)
        arr = [x for bucket in buckets for x in bucket]
    return arr
