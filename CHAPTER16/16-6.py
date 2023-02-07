# Q36 편집 거리

A = input()
B = input()
n = len(A)
m = len(B)

# 최소 거리 계산을 위한 dp 테이블
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# dp 테이블 초기값 설정
for i in range(1, n + 1):
    dp[i][0] = i
for j in range(1, m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 만약 두 문자가 같다면, 왼쪽 위 위치 그대로 삽입
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:  # 다를 경우, 왼쪽(삽입), 위(삭제), 왼쪽 위(교체) 중 최소값에 1을 더한 값을 삽입
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

print(dp[n][m])
