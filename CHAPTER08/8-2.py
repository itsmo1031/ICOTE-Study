# 개미 전사

N = int(input())

food = [*map(int, input().split())]

d = [0] * N

d[0] = food[0]
d[1] = max(food[0], food[1])

for i in range(2, N):
    d[i] = max(d[i - 1], d[i - 2] + food[i])

print(d[N - 1])
