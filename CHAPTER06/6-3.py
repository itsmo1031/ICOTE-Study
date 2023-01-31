# 두 배열의 원소 교체

# N과 K 입력
N, K = map(int, input().split())

# 배열 A와 B 원소 입력. 입력 받으면서 정렬 (A는 오름차순, B는 내림차순)
A = sorted([*map(int, input().split())])
B = sorted([*map(int, input().split())], reverse=True)

# 최대 K번의 연산 수행
for i in range(K):
    # A의 원소가 B의 원소보다 작으면 스위치, 아니라면 탈출
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

# A 배열의 원소의 총합 출력
print(sum(A))
