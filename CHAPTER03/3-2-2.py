n, m, k = map(int, input().split())
num = [*map(int, input().split())]

num.sort(reverse=True)

first = num[0]
second = num[1]

result = m // (k + 1) * (first * k + second) + m % (k + 1) * first

print(result)
