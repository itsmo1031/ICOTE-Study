p = input()
x = int(p[1]) - 1
y = 'abcdefgh'.index(p[0])

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

cnt = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        continue
    cnt += 1

print(cnt)
