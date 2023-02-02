# 떡볶이 떡 만들기

N, M = map(int, input().split())
tteok = [*map(int, input().split())]


def cutting(h):
    result = 0
    for t in tteok:
        if h < t:
            result += t - h
    return result


def cutter(target, start, end):
    global answer
    height = (start + end) // 2
    if end < start:
        return

    if cutting(height) < target:
        cutter(target, start, height - 1)
    else:
        answer = height
        cutter(target, height + 1, end)


answer = 0
cutter(M, 0, max(tteok) - 1)
print(answer)
