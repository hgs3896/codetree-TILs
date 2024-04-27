import sys
from sortedcontainers import SortedSet

input = sys.stdin.readline
s = SortedSet()

def lb(x: int):
    idx = s.bisect_left(x)
    if idx < len(s):
        return s[idx]
    else:
        return None

def ub(x: int):
    idx = s.bisect_right(x)
    if idx < len(s):
        return s[idx]
    else:
        return None

f = {
    'add': lambda x: s.add(x),
    'remove': lambda x: s.remove(x),
    'find': lambda x: print(str(x in s).lower()),
    'lower_bound': lambda x: print(lb(x)),
    'upper_bound': lambda x: print(ub(x)),
    'largest': lambda: print(s[-1] if len(s) else None),
    'smallest': lambda: print(s[0] if len(s) else None),
}

n = int(input())
for _ in range(n):
    args = input().rstrip().split(' ')
    f[args[0]](*args[1:])