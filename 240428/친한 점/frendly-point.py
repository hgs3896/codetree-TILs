import sys
from sortedcontainers import SortedSet

input = sys.stdin.readline
n, m = map(int, input().split())

arr = SortedSet()
for _ in range(n):
    arr.add(tuple(map(int, input().split())))

for _ in range(m):
    # (x = x' & y <= y') or x < x'
    lb = arr.bisect_left(tuple(map(int, input().split())))
    if lb < len(arr):
        print(*arr[lb])
    else:
        print(-1, -1)