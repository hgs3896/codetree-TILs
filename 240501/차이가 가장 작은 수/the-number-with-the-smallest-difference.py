import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(int(input()) for _ in range(n))
l, r = 0, 0
min_diff = arr[-1] - arr[0]
while l < n:
    while r < n and arr[r] - arr[l] < m:
        r += 1
    # Invariant: r == n or arr[r] - arr[l] >= m:
    if r == n:
        break
    # Invariant: arr[r] - arr[l] >= m:
    while l+1 < r and arr[r] - arr[l+1] >= m:
        l += 1
    # Invariant: arr[r] - arr[l] >= m:
    
    min_diff = min(min_diff, arr[r] - arr[l])
    
    l += 1
    # Invariant: arr[r] - arr[l] < m:

if min_diff >= m:
    print(min_diff)
else:
    print(-1)