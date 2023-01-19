n, m, k = map(int, input().split())
num = [*map(int, input().split())]

num.sort(reverse=True)

ans = 0
cnt = 0

for _ in range(m):
    if cnt == k:
        ans += num[1]
        cnt = 0
    else:
        ans += num[0]
        cnt += 1

print(ans)
