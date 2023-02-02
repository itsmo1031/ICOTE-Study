# Q28 고정점 찾기

# 고정점을 이진 탐색으로 구현
def find_fixed_point(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return -1
    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return find_fixed_point(arr, mid + 1, end)
    else:
        return find_fixed_point(arr, start, mid - 1)


N = int(input())
point = [*map(int, input().split())]
print(find_fixed_point(point))
