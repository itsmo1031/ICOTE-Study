# Q19 연산자 끼워 넣기 - DFS 풀이

N = int(input())
nums = [*map(int, input().split())]
add, sub, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9


def dfs(i, now):
    global add, sub, mul, div, max_val, min_val
    if i == N:
        max_val = max(max_val, now)
        min_val = min(min_val, now)
    else:
        if add:
            add -= 1
            dfs(i + 1, now + nums[i])
            add += 1
        if sub:
            sub -= 1
            dfs(i + 1, now - nums[i])
            sub += 1
        if mul:
            mul -= 1
            dfs(i + 1, now * nums[i])
            mul += 1
        if div:
            div -= 1
            dfs(i + 1, int(now / nums[i]))
            div += 1


dfs(1, nums[0])

print(max_val)
print(min_val)
