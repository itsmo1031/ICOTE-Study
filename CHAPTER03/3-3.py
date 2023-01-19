n, m = map(int, input().split())
cards = [[*map(int, input().split())] for _ in range(n)]
result = 0

for card in cards:
    result = max(result, min(card))

print(result)
