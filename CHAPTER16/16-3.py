# Q33 퇴사
# Link: https://www.acmicpc.net/problem/14501

N = int(input())
table = []
for __ in range(N):
    table.append(tuple(map(int, input().split())))

dp = [0] * (N + 1)  # DP 테이블 생성 (마지막날에 1일짜리 상담이 가능하므로 N+1 길이 설정)
max_profit = 0  # 가능한 최대 이익

# 마지막 날부터 거꾸로 내려감
for i in range(N - 1, -1, -1):
    time = i + table[i][0]  # 현재 날짜 + 상담 일수
    if time <= N:
        dp[i] = max(max_profit, table[i][1] + dp[time])
        max_profit = dp[i]
    else:
        dp[i] = max_profit

print(max_profit)
