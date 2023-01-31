# Q23 국영수
# Link: https://www.acmicpc.net/problem/10825

# 학생 정보를 입력받을 data 리스트 선언
data = []

# 입력받은 N만큼의 학생 정보 입력
for __ in range(int(input())):
    n, k, e, m = input().split()
    # 이름, 국어, 영어, 수학 순으로 튜플 형태로 입력
    data.append((n, *map(int, [k, e, m])))

# 국어 내림차순 -> 영어 오름차순 -> 수학 내림차순 -> 이름 오름차순으로 정렬
data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 이름만 출력
for d in data:
    print(d[0])
