from collections import Counter
import heapq
t = int(input())

# change the least frequent elements to the most frequent element k times
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    count = Counter(arr)
    heap = []
    heapq.heapify(heap)
    for num in count.keys():
        heapq.heappush(heap, count[num])
        
    while heap:
        temp = heapq.heappop(heap)
        if temp > k:
            heapq.heappush(heap, count[num])
            break
        k -= temp
        
    return len(heap) if len(heap) != 0 else 1

for i in range(t):
    print(solve())