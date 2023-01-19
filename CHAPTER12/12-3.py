s = input()
result = len(s)

for i in range(1, len(s) + 1):
    subset = [s[j:j + i] for j in range(0, len(s), i)]
    prev = ''
    ts = ''
    cnt = 0
    for sub in subset:
        if prev == sub or prev == '':
            prev = sub
            cnt += 1
        else:
            ts += str(cnt) + prev if cnt != 1 else prev
            prev = sub
            cnt = 1
    ts += str(cnt) + prev if cnt != 1 else prev
    result = min(len(ts), result)

print(result)
