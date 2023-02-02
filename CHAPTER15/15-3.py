# Q29 공유기 설치
# Link: https://www.acmicpc.net/problem/2110

N, C = map(int, input().split())
home = []
for __ in range(N):
    home.append(int(input()))
home.sort()

min_gap = 1
max_gap = home[-1] - home[0]
result = 0

while min_gap <= max_gap:
    mid = (min_gap + max_gap) // 2
    count = 1
    current = home[0]

    # 전체 범위에서 공유기 설치
    for i in range(1, N):
        if home[i] >= current + mid:
            current = home[i]
            count += 1
    if count >= C:  # 설치된 공유기 갯수가 목표보다 같거나 많을 경우
        result = mid
        min_gap = mid + 1  # 최소 갭을 늘려 재확인
    else:
        max_gap = mid - 1  # 최대 갭을 줄여 재확인

print(result)
