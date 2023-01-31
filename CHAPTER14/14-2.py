# Q24 안테나
# Link: https://www.acmicpc.net/problem/18310

N = int(input())

# 집의 정보를 받아 정렬
home = sorted([*map(int, input().split())])

# 중앙값 출력
print(home[(N - 1) // 2])
