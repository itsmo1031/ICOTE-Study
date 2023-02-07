# Q35 못생긴 수

n = int(input())

dp = [0] * n
dp[0] = 1  # 초기값 설정

# 2배, 3배, 5배에 대한 인덱스 및 곱해줄 값 선언
i2 = i3 = i5 = 0
x2 = 2
x3 = 3
x5 = 5

for i in range(1, n):
    # 현재 최솟값을 넣어줌
    dp[i] = min(x2, x3, x5)
    # 모든 같은 값에 대해 인덱스를 1 올려주고 다음 값을 곱해줌으로써 중복되는 값 해결 (elif아닌 if임에 주목)
    if dp[i] == x2:
        i2 += 1
        x2 = dp[i2] * 2
    if dp[i] == x3:
        i3 += 1
        x3 = dp[i3] * 3
    if dp[i] == x5:
        i5 += 1
        x5 = dp[i5] * 5

print(dp.pop())
