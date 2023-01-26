# Q22 블록 이동하기
from collections import deque

b = [[0, 0, 0, 1, 1],
     [0, 0, 0, 1, 0],
     [0, 1, 0, 1, 1],
     [1, 1, 0, 0, 1],
     [0, 0, 0, 0, 0]]

'''
로봇이 할 일:
상, 하, 좌, 우 이동 / 90도 회전 / -90도 회전
'''
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def possible_pos(pos, board):
    possible = []
    p1_x, p1_y = pos[0]
    p2_x, p2_y = pos[1]
    for dx, dy in d:
        np1_x = p1_x + dx
        np1_y = p1_y + dy
        np2_x = p2_x + dx
        np2_y = p2_y + dy
        if board[np1_x][np1_y] == 0 and board[np2_x][np2_y] == 0:
            possible.append({(np1_x, np1_y), (np2_x, np2_y)})
    # 드론이 가로로 있을 때 회전 가능 여부 측정
    if p1_x == p2_x:
        for i in [-1, 1]:
            if board[p1_x + i][p1_y] == 0 and board[p2_x + i][p2_y] == 0:
                possible.append({(p1_x, p1_y), (p1_x + i, p1_y)})
                possible.append({(p2_x, p2_y), (p2_x + i, p2_y)})
    # 드론이 세로로 있을 때 회전 가능 여부 측정
    if p1_y == p2_y:
        for i in [-1, 1]:
            if board[p1_x][p1_y + i] == 0 and board[p2_x][p2_y + i] == 0:
                possible.append({(p1_x, p1_y), (p1_x, p1_y + i)})
                possible.append({(p2_x, p2_y), (p2_x, p2_y + i)})
    return possible


def solution(board):
    # 맵에 벽 두르기
    N = len(board)
    graph = [[1] * (N + 2) for __ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            graph[i + 1][j + 1] = board[i][j]

    # 드론 시작 좌표 설정
    drone = {(1, 1), (1, 2)}
    visited = []
    q = deque()
    visited.append(drone)
    answer = 0
    q.append((drone, answer))
    while q:
        pos, answer = q.popleft()
        if (N, N) in pos:
            return answer
        for p_pos in possible_pos([*pos], graph):
            if p_pos not in visited:
                visited.append(p_pos)
                q.append((p_pos, answer + 1))
    return 0
