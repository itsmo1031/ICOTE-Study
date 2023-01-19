# n덩이 n//2번
s = input()
z = o = 0
piece = 1
while True:
    z = s.find('0')
    o = s.find('1')
    if z == -1 or o == -1:
        break
    else:
        piece += 1
        s = s[abs(z - o):]

print(piece // 2)
