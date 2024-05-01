# rc 1 난이도, 문제 번호 큰 거
# rc -1 난이도 문제 번호 작은 거 출력
# ad P L 난이도 L인 문제번호 P 추가
# sv P L 난이도 L인 문제번호 P 제거
from sortedcontainers import SortedSet
s = SortedSet()
n = int(input())
for _ in range(n):
    p, l = map(int, input().split())
    s.add((l, p))
m = int(input())
for _ in range(m):
    args = input().split()
    if args[0] == "rc":
        if args[1] == "1":
            print(s[-1][1])
        else:
            print(s[0][1])
    else:
        p, l = int(args[1]), int(args[2])
        if args[0] == "ad":
            s.add((l, p))
        else:
            s.remove((l, p))