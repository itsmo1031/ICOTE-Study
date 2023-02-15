# Q40 숨바꼭질
import heapq

INF = int(1e9)
N, M = map(int, input().split())
graph: list[list[tuple]] = [[] for __ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))
    graph[B].append((A, 1))

distance = [INF] * (N + 1)
distance[1] = 0


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for np, nd in graph[now]:
            d = nd + dist
            if d < distance[np]:
                distance[np] = d
                heapq.heappush(q, (d, np))


dijkstra()
far = max(distance[1:])
print(distance.index(far), far, distance.count(far))
