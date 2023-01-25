# Q17 경쟁적 전염

N, K = map(int, input().split())

graph = [[*map(int, input().split())] for _ in range(N)]

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_completed():
    for g in graph:
        if 0 in g:
            return False
    return True


for __ in range(S):
    for i in range(1, K + 1):
        virus = []
        for a in range(N):
            for b in range(N):
                if graph[a][b] == i:
                    virus.append((a, b))
        for v in virus:
            x, y = v
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = i
    if is_completed():
        break

print(graph[X - 1][Y - 1])
