from typing import Tuple, Dict, TypeAlias
from collections import deque

N = int(input())

DR: Tuple[int, int, int, int] = (0, 1, 0,-1)
DC: Tuple[int, int, int, int] = (1, 0,-1, 0)
Coordinate: TypeAlias = Tuple[int, int]

coords: Dict[Coordinate, bool] = {}
for _ in range(N):
    key: Coordinate = tuple(map(int, input().split()))
    coords[key] = -1

visited = {}
def process():
    dq = deque()

    groups = []
    for start in coords:
        if coords[start] != -1:
            continue
        
        group_idx = len(groups)
        groups.append(start)
        
        dq.append(start)
        coords[start] = group_idx
        while dq:
            r, c = dq.popleft()
            for dr, dc in zip(DR, DC):
                nr, nc = r+dr, c+dc
                if (nr, nc) not in coords:
                    continue
                if coords[(nr, nc)] != -1:
                    continue
                groups[-1] = min(groups[-1], (nr, nc))
                dq.append((nr, nc))
                coords[(nr, nc)] = group_idx
    
    count_nearby_edges = lambda r, c: sum((r+dr, c+dc) in coords for dr, dc in zip(DR, DC))
    total_outer_edges = 0
    for key in groups:
        r, c = key
        for dr, dc in zip(DR, DC):
            nr, nc = r+dr, c+dc
            if (nr, nc) in coords:
                continue
            dq.append((nr, nc, 0))
            visited[(nr, nc)] = count_nearby_edges(nr, nc)

        group_outer_edges = 0
        while dq:
            r, c, try_count = dq.popleft()
            
            if try_count > 3:
                continue

            group_outer_edges += visited[(r, c)]
            for dr, dc in zip(DR, DC):
                nr, nc = r+dr, c+dc
                if (nr, nc) in coords:
                    continue
                if (nr, nc) in visited:
                    continue
                visited[(nr, nc)] = count_nearby_edges(nr, nc)
                if visited[(nr, nc)] > 0:
                    dq.append((nr, nc, 0))
                else:
                    dq.append((nr, nc, try_count+1))

        total_outer_edges += group_outer_edges

    return total_outer_edges

print(process())

# def print_coords():
#     min_r = min(coord[0] for coord in coords)
#     max_r = max(coord[0] for coord in coords)
#     min_c = min(coord[1] for coord in coords)
#     max_c = max(coord[1] for coord in coords)
#     for r in range(min_r-1, max_r+2):
#         for c in range(min_c-1, max_c+2):
#             print(chr(ord('A')+coords[(r,c)]) if (r, c) in coords else visited.get((r, c), 'x'), end='')
#         print()

# print_coords()