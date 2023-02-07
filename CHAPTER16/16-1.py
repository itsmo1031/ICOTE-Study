# Q31 금광

for __ in range(int(input())):
    n, m = map(int, input().split())

    mine = [*map(int, input().split())]

    d = []

    for k in range(n):
        d.append(mine[k * m:(k + 1) * m])

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = d[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = d[i + 1][j - 1]
            left = d[i][j - 1]
            d[i][j] += max(left_up, left, left_down)

    result = 0
    for x in range(n):
        result = max(result, d[x][m - 1])

    print(result)
