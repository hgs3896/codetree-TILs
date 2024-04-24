# (k-1/k) 초대장 받음 -> 나머지 1명도 받음
from collections import deque, defaultdict
import sys

input = sys.stdin.readline

N, G = map(int, input().split())
members_per_group = {}
group_per_member = defaultdict(list)
for g in range(1, G+1):
    _, *members = map(int, input().split())
    members_per_group[g] = set(members)
    for v in members:
        group_per_member[v].append(g)

q = deque([1])
removed = set()
removed.add(1)

while q:
    v = q.popleft()
    for g in group_per_member[v]:
        if v not in members_per_group[g]:
            continue
        members_per_group[g].remove(v)
        if len(members_per_group[g]) != 1:
            continue
        w = members_per_group[g].__iter__().__next__()
        if w in removed:
            continue
        removed.add(w)
        q.append(w)
    del group_per_member[v]
print(len(removed))