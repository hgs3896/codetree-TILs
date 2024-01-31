from typing import Tuple, Dict, TypeAlias
from collections import deque
import sys

input = sys.stdin.readline

Coordinate: TypeAlias = Tuple[int, int]

N: int = int(input())
DR: Tuple[int, int, int, int] = (0, 1, 0,-1)
DC: Tuple[int, int, int, int] = (1, 0,-1, 0)

coords: Dict[Coordinate, bool] = {}
for _ in range(N):
    key: Coordinate = tuple(map(int, input().split()))
    coords[key] = False

def process():
    dq = deque()

    # Traverse groups by BFS
    groups = []
    for start in coords:
        if coords[start]:
            continue
        groups.append(start)

        dq.append(start)
        coords[start] = True
        while dq:
            r, c = dq.popleft()
            for dr, dc in zip(DR, DC):
                nr, nc = r+dr, c+dc
                if (nr, nc) not in coords:
                    continue
                if coords[(nr, nc)]:
                    continue
                groups[-1] = min(groups[-1], (nr, nc))
                dq.append((nr, nc))
                coords[(nr, nc)] = True
    
    count_nearby_groups = lambda r, c: sum((r+dr, c+dc) in coords for dr, dc in zip(DR, DC))
    has_any_groups = lambda r, c: any((r+dr, c+dc) in coords for dr in range(-1, 2) for dc in range(-1, 2) if (dr, dc) != (0, 0))

    total_outer_edges = 0
    visited = set()
    for key in groups:
        r, c = key
        for dr, dc in zip(DR, DC):
            nr, nc = r+dr, c+dc
            if (nr, nc) in coords:
                continue
            dq.append((nr, nc))
            visited.add((nr, nc))

        group_outer_edges = 0
        while dq:
            r, c = dq.popleft()

            group_outer_edges += count_nearby_groups(r, c)
            for dr, dc in zip(DR, DC):
                nr, nc = r+dr, c+dc
                if (nr, nc) in coords:
                    continue
                if (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                if has_any_groups(nr, nc):
                    dq.append((nr, nc))

        total_outer_edges += group_outer_edges

    return total_outer_edges

print(process())