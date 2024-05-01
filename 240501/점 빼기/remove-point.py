from sortedcontainers import SortedSet
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
:
s = SortedSet(tuple(map(int, input().split())) for _ in range(n))
for _ in range(m):
    idx = s.bisect_left((int(input()), 0))
    if idx == len(s):
        print(-1, -1)
    else:
        print(*s[idx])
        s.remove(s[idx])