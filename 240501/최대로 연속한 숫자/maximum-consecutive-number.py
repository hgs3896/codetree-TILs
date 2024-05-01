from sortedcontainers import SortedSet
from heapq import heappush, heappop
n, m = map(int, input().split())

removed_interval = set()
intervals = SortedSet()
intervals.add((0, n))

interval_heap = [(-(n-0+1), 0, n)]

for x in map(int, input().split()):
    idx = intervals.bisect_left((x+1, 0)) - 1
    
    l, r = intervals[idx]
    intervals.remove(intervals[idx])
    removed_interval.add((l, r))
    
    if l <= x-1:
        intervals.add((l, x-1))
        heappush(interval_heap, (-(x-l), l, x-1))
    if x+1 <= r:
        intervals.add((x+1, r))
        heappush(interval_heap, (-(r-x), x+1, r))
    
    while interval_heap and (interval_heap[0][1], interval_heap[0][2]) in removed_interval:
        heappop(interval_heap)
    print(-interval_heap[0][0])