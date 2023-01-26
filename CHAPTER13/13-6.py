# Q20 감시 피하기
from itertools import combinations
import copy

N = int(input())
hallway = [[*input().split()] for _ in range(N)]
empty = []
teacher = []
student = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N):
    for j in range(N):
        if hallway[i][j] == 'X':
            empty.append((i, j))
        if hallway[i][j] == 'T':
            teacher.append((i, j))
        if hallway[i][j] == 'S':
            student += 1


def watch(pos):
    for d in range(4):
        x, y = pos
        if d == 0:
            while y >= 0:
                if temp[x][y] == 'O':
                    break
                else:
                    temp[x][y] = 'T'
                y -= 1
        if d == 1:
            while y < N:
                if temp[x][y] == 'O':
                    break
                else:
                    temp[x][y] = 'T'
                y += 1
        if d == 2:
            while x >= 0:
                if temp[x][y] == 'O':
                    break
                else:
                    temp[x][y] = 'T'
                x -= 1
        if d == 3:
            while x < N:
                if temp[x][y] == 'O':
                    break
                else:
                    temp[x][y] = 'T'
                x += 1


def cnt_student(graph):
    std = 0
    for x in range(N):
        for y in range(N):
            if graph[x][y] == 'S':
                std += 1
    return std


result = 'NO'

for possible in combinations(empty, 3):
    # 초기 맵 설정
    temp = copy.deepcopy(hallway)
    for p in possible:
        temp[p[0]][p[1]] = 'O'

    for t in teacher:
        watch(t)

    if student == cnt_student(temp):
        result = 'YES'
        break

print(result)
