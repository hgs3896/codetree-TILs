from functools import cache

N, B = map(int, input().split())
s = sum(int(input()) << (N-1-i) for i in range(N))

@cache
def get_next_state(s: int): # O(N)
    return s ^ ((((s & 1) << N) | s) >> 1)
    # ns = 0
    # for i in range(N):
    #     if s & (1 << (i+1)%N):
    #         ns |= (1 - ((s >> i) & 1)) << i
    #     else:
    #         ns |= s & (1 << i)
    # return ns

@cache
def composition(s, rep):
    if rep % 2 == 1:
        s = get_next_state(s)
        rep -= 1
    if rep == 0:
        return s
    rep //= 2
    s = composition(s, rep)
    s = composition(s, rep)
    return s

s = composition(s, B)
for i in range(N):
    print(int(s & (1 << (N-1-i)) != 0))