n, m = map(int, input().split())
x, y, d = map(int, input().split())
info = [[*map(int, input().split())] for _ in range(n)]
visited = [[0] * m for _ in range(n)]
# 북/동/남/서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn():
    global d
    d -= 1
    if d == -1:
        d = 3


visited[x][y] = 1
cnt = 1
turned = 0
while True:
    turn()
    nx = x + dx[d]
    ny = y + dy[d]
    if info[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turned = 0
        continue
    else:
        turned += 1
    if turned == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if info[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turned = 0

print(cnt)
