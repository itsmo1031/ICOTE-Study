from collections import deque

n = int(input())

# 오른쪽부터 시계방향 회전
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def change_direction(d):
    global sd
    if d == 'D':
        sd += 1
        if sd == 4:
            sd = 0
    elif d == 'L':
        sd -= 1
        if sd == -1:
            sd = 3


# 벽이 있는 보드 만들기
board = [[1] * (n + 2) for _ in range(n + 2)]
for i in range(n):
    for j in range(n):
        board[i + 1][j + 1] -= 1

# 뱀(1) 좌표 입력
snake = deque([(1, 1)])
sd = 0

# 사과(2) 좌표 입력
for _ in range(int(input())):
    x, y = map(int, input().split())
    board[x][y] = 2


# 트리거 입력
def start_game():
    cur_time = 0
    command = deque()
    for _ in range(int(input())):
        ti, di = input().split()
        command.append((int(ti), di))

    while True:
        cur_time += 1
        tx = snake[-1][0] + dx[sd]
        ty = snake[-1][1] + dy[sd]
        if board[tx][ty] == 1 or (tx, ty) in snake:
            return print(cur_time)
        elif board[tx][ty] == 2:
            snake.append((tx, ty))
            board[tx][ty] = 0
        elif board[tx][ty] == 0:
            snake.popleft()
            snake.append((tx, ty))
        if command:
            if cur_time == command[0][0]:
                change_direction(command[0][1])
                command.popleft()


start_game()
