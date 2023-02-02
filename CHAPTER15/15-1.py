# Q24 정렬된 배열에서 특정 수의 개수 구하기 - bisect 직접 구현


# 지정된 숫자의 제일 왼쪽 인덱스 이진 탐색으로 구현
def bs_left(arr, target, start=0, end=None, result=-1):
    if end is None:
        end = len(arr) - 1
    if end < start:
        return result
    mid = (start + end) // 2

    # 현재 값이 찾는 값이면 리턴할 값에 저장
    if arr[mid] == target:
        result = mid

    # 현재 값이 목표 값보다 작을 때만 오른쪽 탐색, 같거나 크면 왼쪽 추가 탐색
    if arr[mid] < target:
        return bs_left(arr, target, mid + 1, end, result)
    else:
        return bs_left(arr, target, start, mid - 1, result)


# 지정된 숫자의 제일 오른쪽 인덱스+1 리턴
def bs_right(arr, target, start=0, end=None, result=-1):
    if end is None:
        end = len(arr) - 1
    if end < start:
        return result + 1
    mid = (start + end) // 2

    # 현재 값이 찾는 값이면 리턴할 값에 저장
    if arr[mid] == target:
        result = mid

    # 현재 값이 목표 값보다 클 때만 왼쪽 탐색, 같거나 작으면 오른쪽 추가 탐색
    if arr[mid] > target:
        return bs_right(arr, target, start, mid - 1, result)
    else:
        return bs_right(arr, target, mid + 1, end, result)


N, x = map(int, input().split())
num = [*map(int, input().split())]
left_idx = bs_left(num, x)
right_idx = bs_right(num, x)
if left_idx == -1:
    print(-1)
else:
    print(right_idx - left_idx)
