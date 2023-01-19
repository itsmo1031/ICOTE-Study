n = int(input())
users = [*map(int, input().split())]
users.sort()
count = result = 0

for user in users:
    count += 1  # 그룹 인원 1명 추가
    if count >= user:  # 만약 그룹 인원이 현재 인원의 공포 이상이면
        result += 1  # 그룹 결성
        count = 0  # 그룹 인원 초기화

print(result)
