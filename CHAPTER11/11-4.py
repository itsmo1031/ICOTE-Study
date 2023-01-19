n = int(input())
coins = [*map(int, input().split())]
coins.sort()
result = 1
for coin in coins:
    if result < coin:
        break
    result += coin

print(result)
