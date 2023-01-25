# Q19 연산자 끼워 넣기
# TODO: DFS/BFS로 다시 풀기

from itertools import permutations
from collections import deque
import copy

n = int(input())
nums = deque([*map(int, input().split())])
plus, minus, multiply, divide = map(int, input().split())
operator = []
operator += ['+'] * plus
operator += ['-'] * minus
operator += ['*'] * multiply
operator += ['/'] * divide

min_result = 1e9 + 1
max_result = -min_result

for op in permutations(operator, n - 1):
    temp = copy.deepcopy(nums)
    for i in range(n - 1):
        a = temp.popleft()
        b = temp.popleft()
        if op[i] == '+':
            temp.appendleft(a + b)
        elif op[i] == '-':
            temp.appendleft(a - b)
        elif op[i] == '*':
            temp.appendleft(a * b)
        elif op[i] == '/':
            t = abs(a) // abs(b)
            if a < 0 or b < 0:
                temp.appendleft(-t)
            else:
                temp.appendleft(t)
    max_result = max(max_result, temp[0])
    min_result = min(min_result, temp[0])

print(max_result)
print(min_result)
