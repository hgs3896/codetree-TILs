from collections import defaultdict, deque
from heapq import heappush, heappop, heapify

def calculate_costs(s, g):
    d = {s: 0}
    
    h = [(0, s)]
    visited = set()
    while h:
        dist, u = heappop(h)
        if u in visited:
            continue
        visited.add(u)
        for v, w in g[u].items():
            if v in visited:
                continue
            if d.get(v, float('inf')) <= dist + w:
                continue
            d[v] = dist + w
            heappush(h, (dist + w, v))
    # print(d)
    return d

Q = int(input())
G = defaultdict(lambda:defaultdict(lambda:20_0000_0000))
travels = {}

S = 0
costs = {}
profits = []

for _ in range(Q):
    args = list(map(int, input().split()))
    if args[0] == 100:
        n, m, *data = args[1:]
        for i in range(0, 3*m, 3):
            u, v, w = data[i:i+3]
            w = min(w, G[u][v])
            G[u][v] = G[v][u] = w
        
        costs[S] = calculate_costs(S, G)
    elif args[0] == 200:
        tid, rev, dst = args[1:]
        travels[tid] = (rev, dst)

        if dst in costs[S]:
            cost = costs[S][dst]
            heappush(profits, (-(rev-cost), tid))

    elif args[0] == 300:
        tid = args[1]
        if tid in travels:
            del travels[tid]
    elif args[0] == 400:
        # 최적 여행 상품 id 출력
        while profits and profits[0][1] not in travels:
            heappop(profits)
        if profits and profits[0][0] <= 0:
            print(profits[0][1])
            del travels[profits[0][1]]
            heappop(profits)
        else:
            print(-1)
    else:
        S = args[1]
        if S not in costs:
            costs[S] = calculate_costs(S, G)
        
        profits = [
            (-(rev-costs[S][dst]), tid)
            for tid, (rev, dst) in travels.items()
            if dst in costs[S]
        ]
        heapify(profits)