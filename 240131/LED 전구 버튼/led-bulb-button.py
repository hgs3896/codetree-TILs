import sys
from functools import cache
from collections import OrderedDict

input = sys.stdin.readline
N, B = map(int, input().split())
s = sum(int(input()) << (N-1-i) for i in range(N))

@cache
def get_next_state(s: int): # O(1)
    return s ^ ((((s & 1) << N) | s) >> 1)

# @cache
# def get_next_state(s: int): # O(N)
    # ns = 0
    # for i in range(N):
    #     if s & (1 << (i+1)%N):
    #         ns |= (1 - ((s >> i) & 1)) << i
    #     else:
    #         ns |= s & (1 << i)
    # return ns

def composition(s: int, rep: int):
    S = OrderedDict()
    for idx in range(rep):
        if s in S:
            break
        S[s] = idx
        s = get_next_state(s)
    if s not in S:
        return s
    cycle_length = len(S) - S[s]
    idx = (rep - S[s]) % cycle_length + S[s]
    for k, v in S.items():
        if v == idx:
            return k

# @cache
# def composition(s: int, rep: int):
#     if rep % 2 == 1:
#         s = get_next_state(s)
#         rep -= 1
    
#     if rep == 0:
#         return s

#     rep //= 2
#     s = composition(s, rep)
#     s = composition(s, rep)
#     return s

s = composition(s, B)
for i in range(N):
    print(int(s & (1 << (N-1-i)) != 0))