# 커리큘럼
from collections import deque
from copy import deepcopy

N = int(input())
# 진입차선 초기화
indegree = [0] * (N + 1)

graph: list[list[int]] = [[] for __ in range(N + 1)]
# 강의시간 초기화
time = [0] * (N + 1)

# 간선 정보 입력
for i in range(1, N + 1):
    data = [*map(int, input().split())]
    time[i] = data[0]  # 첫번째 값 = 시간
    for x in data[1:-1]:  # 두번째 값부터 -1 이전 값까지
        indegree[i] += 1  # 선수과목 수만큼 진입차수 올림
        graph[x].append(i)


def topology_sort():
    result = deepcopy(time)
    q = deque()

    for a in range(1, N + 1):
        if indegree[a] == 0:
            q.append(a)

    while q:
        now = q.popleft()
        for k in graph[now]:
            result[k] = max(result[k], result[now] + time[k])
            indegree[k] -= 1
            if indegree[k] == 0:
                q.append(k)

    for r in range(1, N + 1):
        print(result[r])


topology_sort()
