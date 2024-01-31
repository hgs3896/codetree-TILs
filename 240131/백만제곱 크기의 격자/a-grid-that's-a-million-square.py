from typing import Tuple, Dict, TypeAlias, Generator
from collections import deque
import sys

input = sys.stdin.readline

Coordinate: TypeAlias = Tuple[int, int]
CoordinateGenerator: TypeAlias = Generator[Coordinate, None, None]

N: int = int(input())
DR: Tuple[int, int, int, int] = (0, 1, 0,-1)
DC: Tuple[int, int, int, int] = (1, 0,-1, 0)

def read_coordinates() -> Dict[Coordinate, bool]:
    coords: Dict[Coordinate, bool] = {}
    for _ in range(N):
        key: Coordinate = tuple(map(int, input().split()))
        coords[key] = False
    return coords

def process(coords: Dict[Coordinate, bool]):
    dq = deque()
    visited = set()

    def around(r, c) -> CoordinateGenerator:
        for dr, dc in zip(DR, DC):
            nr, nc = r+dr, c+dc
            if (nr, nc) in coords:
                continue
            yield nr, nc

    def exceptCoord(g: CoordinateGenerator) -> CoordinateGenerator:
        for r, c in g:
            if (r, c) in coords:
                continue
            yield r, c

    def exceptVisited(g: CoordinateGenerator) -> CoordinateGenerator:
        for r, c in g:
            if (r, c) in visited:
                continue
            yield r, c

    # Traverse groups by BFS
    # O(V+E) = O(V)
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
    
    # Count outer groups by multi-starting points BFS
    total_outer_groups = 0
    for group_coord in groups:
        for nr, nc in exceptCoord(around(*group_coord)):
            dq.append((nr, nc))
            visited.add((nr, nc))

    while dq:
        r, c = dq.popleft()

        total_outer_groups += count_nearby_groups(r, c)
        for nr, nc in exceptVisited(exceptCoord(around(r, c))):
            visited.add((nr, nc))
            if has_any_groups(nr, nc):
                dq.append((nr, nc))

    return total_outer_groups

print(process(read_coordinates()))