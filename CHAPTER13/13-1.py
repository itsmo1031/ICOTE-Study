from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

distance = [-1] * (N + 1)
distance[X] = 0

q = deque([X])

while q:
    now = q.popleft()
    for city in graph[now]:
        if distance[city] == -1:
            distance[city] = distance[now] + 1
            q.append(city)

check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if not check:
    print(-1)
