from sortedcontainers import SortedSet
import sys

input = lambda: sys.stdin.readline().rstrip()
s = SortedSet()
T = int(input())
for _ in range(T):
    k = int(input())
    for _ in range(k):
        args = input().split(' ')
        if args[0] == 'I':
            s.add(int(args[1]))
        elif s:
            if args[1] == '1':
                s.remove(s[-1])
            else:
                s.remove(s[0])
    if s:
        print(s[-1], s[0])
    else:
        print("EMPTY")