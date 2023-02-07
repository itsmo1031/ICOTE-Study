# Q32 정수 삼각형
# Link: https://www.acmicpc.net/problem/1932

n = int(input())
tri = []
for __ in range(n):
    tri.append([*map(int, input().split())])

for i in range(1, n):
    for j in range(len(tri[i])):
        if j == 0:
            tri[i][j] += tri[i - 1][j]
        elif j == len(tri[i]) - 1:
            tri[i][j] += tri[i - 1][j - 1]
        else:
            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

print(max(tri[n - 1]))
