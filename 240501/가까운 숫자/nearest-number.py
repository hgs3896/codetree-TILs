from sortedcontainers import SortedSet
input()
s = SortedSet()
s.add(0)
min_dist = 100000
for x in map(int, input().split()):
    r = s.bisect_right(x)
    dist = x - s[r-1]
    if r < len(s):
        dist = min(dist, s[r] - x)
    min_dist = min(min_dist, dist)
    s.add(x)
    print(min_dist)