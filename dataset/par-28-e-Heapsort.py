import heapq

def heapsort_alt(arr):
    max_heap = [-x for x in arr]  # convertir a max-heap
    heapq.heapify(max_heap)
    result = [-heapq.heappop(max_heap) for _ in range(len(arr))]
    return result
