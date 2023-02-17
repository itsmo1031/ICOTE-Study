# Q45 최종 순위
# Link: https://www.acmicpc.net/problem/3665

from collections import deque


def topology_sort():
    result = []
    q = deque()

    # 진입차수 0인 노드 삽입
    for k in range(1, n + 1):
        if indegree[k] == 0:
            q.append(k)

    unique = True  # 결과가 유일해야 함
    cycle = False  # 사이클이 없어야 함

    # q가 빌때까지가 아닌 n번 수행
    for __ in range(n):
        if len(q) == 0:
            # q가 0일 경우 사이클이 발생한 것
            cycle = True
            break
        elif len(q) >= 2:
            # q에 2개 이상이 들어갈 경우 해가 유일하지 않은 것
            unique = False
            break
        now = q.popleft()
        result.append(now)
        for x in range(1, n + 1):
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)

    if cycle:
        return "IMPOSSIBLE"
    if not unique:
        return "?"
    return " ".join(map(str, result))


for __ in range(int(input())):
    n = int(input())
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for __ in range(n + 1)]

    # 순위 입력받음 (1위부터 순서대로)
    data = [*map(int, input().split())]
    for i in range(n):
        for j in range(i + 1, n):
            # 자기보다 순위가 낮은 팀을 가르키도록 설정
            graph[data[i]][data[j]] = True
            # 순위가 낮은 팀의 차수 증가
            indegree[data[j]] += 1

    # 올해 변경된 순위 입력
    for __ in range(int(input())):
        a, b = map(int, input().split())
        # 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[b] += 1
            indegree[a] -= 1

    print(topology_sort())
