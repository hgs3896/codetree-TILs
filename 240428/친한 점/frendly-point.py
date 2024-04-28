from sortedcontainers import SortedSet

n, m = map(int, input().split())

arr = SortedSet()
for _ in range(n):
    x, y = map(int, input().split())
    arr.add((x, y))

for _ in range(m):
    x, y = map(int, input().split())
    # (x = x' & y <= y') or x < x'
    lb = arr.bisect_left((x, y))
    if lb < len(arr):
        print(*arr[lb])
    else:
        print(-1, -1)