# 미래 도시
INF = int(1e9)
N, M = map(int, input().split())

graph = [[INF] * (N + 1) for __ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for __ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

# 플로이드 워셜 알고리즘 숳애
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][K] + graph[K][X]

print(result if result < INF else -1)
