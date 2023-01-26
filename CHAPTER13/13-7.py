# Q21 인구 이동
from collections import deque

N, L, R = map(int, input().split())
cities = [[*map(int, input().split())] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def finding(city):
    q = deque([city])
    union = [city]
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(cities[nx][ny] - cities[x][y]) <= R:
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    q.append((nx, ny))
    return union if len(union) > 1 else []


unions = []
result = 0
while True:
    unions.clear()
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                u = finding((i, j))
                if u:
                    unions.append(u)
    if not unions:
        break
    for c in unions:
        tmp = 0
        for a, b in c:
            tmp += cities[a][b]
        tmp //= len(c)
        for a, b in c:
            cities[a][b] = tmp
    result += 1

print(result)
