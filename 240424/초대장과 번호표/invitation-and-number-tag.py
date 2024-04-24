# (k-1/k) 초대장 받음 -> 나머지 1명도 받음
from collections import deque, defaultdict
N, G = map(int, input().split())
members_per_group = {}
group_per_member = defaultdict(list)
for g in range(1, G+1):
    _, *members = map(int, input().split())
    members_per_group[g] = set(members)
    for v in members:
        group_per_member[v].append(g)

q = deque([1])
cnt = 0
while q:
    v = q.popleft()
    cnt += 1
    for g in group_per_member[v]:
        if v in members_per_group[g]:
            members_per_group[g].remove(v)
            if len(members_per_group[g]) == 1:
                q.append(members_per_group[g].__iter__().__next__())
print(cnt)