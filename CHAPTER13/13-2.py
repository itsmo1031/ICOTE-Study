# TODO: DFS로 다시 풀어보기

from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(n)]
temp = [[0] * m for _ in range(n)]
empty = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def virus(x, y):
    q = deque([(x, y)])
    while q:
        ix, iy = q.popleft()
        for c in range(4):
            nx = ix + dx[c]
            ny = iy + dy[c]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp[nx][ny] == 0:
                q.append((nx, ny))
                temp[nx][ny] = 2


def get_zero():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt


result = 0

for possible in combinations(empty, 3):
    # temp 맵 초기화
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j]
    for p in possible:
        temp[p[0]][p[1]] = 1

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                virus(i, j)
    result = max(result, get_zero())

print(result)
