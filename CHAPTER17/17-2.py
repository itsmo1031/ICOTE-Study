# Q38 정확한 순위
INF = int(1e9)
N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for x in range(1, N + 1):
    graph[x][x] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
for i in range(1, N + 1):
    cnt = 0  # 도달 가능한 수
    for j in range(1, N + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == N:  # 모든 노드에서 도달 가능하면 결과 추가
        result += 1

print(result)
