def sample_sort(arr, num_buckets=4):
    if not arr:
        return arr
    samples = sorted(arr[::len(arr)//num_buckets])
    buckets = [[] for _ in range(num_buckets)]
    
    for val in arr:
        for i in range(len(samples)):
            if val <= samples[i]:
                buckets[i].append(val)
                break
        else:
            buckets[-1].append(val)
    
    sorted_arr = []
    for b in buckets:
        sorted_arr.extend(sorted(b))
    return sorted_arr
