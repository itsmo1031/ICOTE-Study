s = input()
n = 0
a = []
for k in s:
    if k in '1234567890':
        n += int(k)
    else:
        a.append(k)
a.sort()
print(''.join(a) + str(n))
