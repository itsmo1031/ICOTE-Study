from functools import reduce

n = input()
h = len(n) // 2
left = n[:h]
right = n[h:]


def summary(arr):
    return reduce(lambda x, y: int(x) + int(y), arr)


if summary(left) == summary(right):
    print("LUCKY")
else:
    print("READY")
