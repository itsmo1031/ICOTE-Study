# Q39 화성 탐사
import heapq

INF = int(1e9)

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# 다익스트라 정의
def dijkstra():
    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        dist, x, y = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                nd = dist + graph[nx][ny]
                if nd < distance[nx][ny]:
                    distance[nx][ny] = nd
                    heapq.heappush(q, (nd, nx, ny))

    return distance[N - 1][N - 1]


for __ in range(int(input())):
    N = int(input())
    graph = [[*map(int, input().split())] for __ in range(N)]
    distance = [[INF] * N for __ in range(N)]

    print(dijkstra())
