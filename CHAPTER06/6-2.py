# 성적이 낮은 순서로 학생 출력하기

# 학생과 성적을 담을 리스트 선언
arr = []

# 주어진 N개의 수 만큼 학생과 성적 정보 입력
for __ in range(int(input())):
    data = input().split()
    # 튜플(이름, 성적)형태로 리스트에 추가
    # 성적은 int 형변환
    arr.append((data[0], int(data[1])))

# 성적 오름차순으로 리스트 정렬
arr.sort(key=lambda x: x[1])

# 성적순 이름만 출력
print(*[*zip(*arr)][0])
