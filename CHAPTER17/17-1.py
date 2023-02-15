# Q37 플로이드
# Link: https://www.acmicpc.net/problem/11404
INF = int(1e9)

n = int(input())
m = int(input())
distance = [[INF] * n for _ in range(n)]

for x in range(n):
    distance[x][x] = 0

for __ in range(m):
    a, b, c = map(int, input().split())
    distance[a - 1][b - 1] = min(distance[a - 1][b - 1], c)

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# 갈수 없는 경우 0으로 설정
for i in range(n):
    for j in range(n):
        if distance[i][j] == INF:
            distance[i][j] = 0

for d in distance:
    print(*d)
