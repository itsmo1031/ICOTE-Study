s = input()

result = 0

if len(s) == 1:
    result = int(s)
else:
    if s[0] == '0' or s[0] == '1' or s[1] == '0' or s[1] == '1':
        result = int(s[0]) + int(s[1])
    else:
        result = int(s[0]) * int(s[1])
    if len(s) > 2:
        for i in range(2, len(s)):
            if s[i] == '0' or s[i] == '1':
                result += int(s[i])
            else:
                result *= int(s[i])
print(result)
