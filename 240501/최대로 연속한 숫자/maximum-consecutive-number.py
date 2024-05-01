from sortedcontainers import SortedSet
n, m = map(int, input().split())

removed = SortedSet()
removed.add((0, n))
max_length = n+1

for x in map(int, input().split()):
    idx = removed.bisect_left((x+1, 0)) - 1
    
    l, r = removed[idx]
    removed.remove(removed[idx])
    
    if l <= x-1:
        removed.add((l, x-1))
    if x+1 <= r:
        removed.add((x+1, r))
    
    if max_length == r-l+1:
        max_length = max(rr-ll+1 for ll, rr in removed)
    print(max_length)