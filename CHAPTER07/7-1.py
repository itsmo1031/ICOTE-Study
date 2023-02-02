# 부품 찾기

def binary_search(arr, target, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2

    if arr[mid] == target:
        return "yes"
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


N = int(input())
part = [*map(int, input().split())]
M = int(input())
req = [*map(int, input().split())]

for r in req:
    print(binary_search(part, r, 0, len(part) - 1))
