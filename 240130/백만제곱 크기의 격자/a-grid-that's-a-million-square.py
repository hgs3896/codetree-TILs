from typing import Tuple

N = int(input())

disjoint_set = {}
def make_set(key: Tuple[int, int]):
    disjoint_set[key] = key
    return disjoint_set[key]

def find_parent(key: Tuple[int, int]):
    children = []
    while key != disjoint_set[key]:
        children.append(key)
        key = disjoint_set[key]
    # path compression
    for c in children:
        disjoint_set[c] = key
    return key

def merge(a: Tuple[int, int], b: Tuple[int, int]):
    disjoint_set[b] = a

DR = (0, 1, 0,-1)
DC = (1, 0,-1, 0)

for _ in range(N):
    a, b = map(int, input().split())
    key = (a, b)
    s = make_set(key)
    p = find_parent(s)
    for dr, dc in zip(DR, DC):
        adjacent_key = (a + dr, b + dc)
        if adjacent_key not in disjoint_set:
            continue
        merge(p, find_parent(disjoint_set[adjacent_key]))

group_info = {}
for key in disjoint_set:
    r, c = key
    key = find_parent(key)
    if key not in group_info:
        group_info[key] = [1000001, 1000001, 0, 0]
    group_info[key][0] = min(group_info[key][0], r)
    group_info[key][1] = min(group_info[key][1], c)
    group_info[key][2] = max(group_info[key][2], r)
    group_info[key][3] = max(group_info[key][3], c)

print(
    sum(
        2 * (info[2]-info[0]+1+info[3]-info[1]+1)
        for info in group_info.values()
    )
)