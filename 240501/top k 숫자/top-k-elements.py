from heapq import heapify, heappop
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(set(map(lambda v: -int(v), input().split())))
heapify(arr)
for v in range(k):
    print(-heappop(arr), end=' ')
print()