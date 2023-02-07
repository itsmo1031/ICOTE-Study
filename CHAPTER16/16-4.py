# Q34 병사 배치하기
# Link: https://www.acmicpc.net/problem/18353

N = int(input())
soldier = [*map(int, input().split())]
d = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if soldier[i] < soldier[j]:
            d[i] = max(d[i], d[j] + 1)

print(N - max(d))
