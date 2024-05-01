import sys
from sortedcontainers import SortedSet
input = sys.stdin.readline

n, m = map(int, input().split())
s = SortedSet(range(1, m+1))
for x in map(int, input().split()):
    s.remove(x)
    print(s[-1])