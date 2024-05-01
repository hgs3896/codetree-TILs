n, m = map(int, input().split())
arr = sorted(int(input()) for _ in range(n))
l, r = 0, 0
min_diff = arr[-1] - arr[0]
while l < n:
    while r < n and arr[r] - arr[l] < m:
        r += 1
    if r == n:
        break
    min_diff = min(min_diff, arr[r] - arr[l])
    while l < r and arr[r] - arr[l] >= m:
        l += 1
if min_diff < m:
    print(-1)
else:
    print(min_diff)