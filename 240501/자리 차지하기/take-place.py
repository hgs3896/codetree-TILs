from sortedcontainers import SortedSet

# a_i번 이하 의자 중에 앉을 수 있는 것 찾기
n, m = map(int, input().split())
s = SortedSet(range(1, m+1))

for a_i in map(int, input().split()):
    idx = s.bisect_right(a_i) - 1
    if idx < 0:
        break
    s.remove(s[idx])
print(m-len(s))