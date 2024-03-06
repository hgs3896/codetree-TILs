N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]
cnt = 0
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            s = set()
            possible = True
            for arr in A:
                s.add((arr[i], arr[j], arr[k]))
            for arr in B:
                if (arr[i], arr[j], arr[k]) in s:
                    possible = False
                    break
            if possible:
                cnt += 1

print(cnt)