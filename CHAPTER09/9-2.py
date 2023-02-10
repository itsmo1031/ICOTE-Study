# 전보

import heapq

INF = int(1e9)
N, M, C = map(int, input().split())
graph = [[] for __ in range(N + 1)]
dist = [INF] * (N + 1)

for __ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

q = []
heapq.heappush(q, (0, C))
dist[C] = 0
while q:
    d, now = heapq.heappop(q)
    if dist[now] < d:
        continue
    for np, nd in graph[now]:
        cost = d + nd
        if cost < dist[np]:
            dist[np] = cost
            heapq.heappush(q, (cost, np))

count = -1
max_d = 0
for d in dist:
    if d != INF:
        count += 1
        max_d = max(max_d, d)

print(count, max_d)
