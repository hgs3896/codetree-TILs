N, K = map(int, input().split())
S = list(range(N))
V = list({i} for i in range(N))
items = []
for _ in range(K):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    items.append((a, b))
for _ in range(3):
    for a, b in items:
        S[a], S[b] = S[b], S[a]
        V[S[a]].add(a)
        V[S[b]].add(b)
for s in V:
    print(len(s))