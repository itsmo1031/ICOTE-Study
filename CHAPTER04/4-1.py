n = int(input())
x = y = 1
directions = input().split()

for d in directions:
    if d == 'L':
        if y > 1:
            y -= 1
    if d == 'R':
        if y < n:
            y += 1
    if d == 'U':
        if x > 1:
            x -= 1
    if d == 'D':
        if x < n:
            x += 1

print(x, y)
