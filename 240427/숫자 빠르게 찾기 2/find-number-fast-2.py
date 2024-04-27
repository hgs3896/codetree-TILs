from sortedcontainers import SortedSet
import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split(' '))
s = SortedSet(map(int, input().split(' ')))
for _ in range(m):
    idx = s.bisect_left(int(input()))
    if idx < len(s):
        print(s[idx])
    else:
        print(-1)