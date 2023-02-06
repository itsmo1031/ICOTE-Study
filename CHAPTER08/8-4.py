# 효율적인 화폐 구성

N, M = map(int, input().split())
coin = []
for __ in range(N):
    coin.append(int(input()))

d = [10001] * (M + 1)

d[0] = 0

for c in coin:
    for i in range(c, M + 1):
        d[i] = min(d[i], d[i - c] + 1)

print(d[M] if d[M] != 10001 else -1)
