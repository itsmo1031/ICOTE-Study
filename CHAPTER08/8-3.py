# 바닥 공사

N = int(input())

d = [0] * N

d[0] = 1
d[1] = 3

for i in range(2, N):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[N - 1])
