# 도시 분할 계획
# Link: https://www.acmicpc.net/problem/1647


# 특정 원소의 루트 노드 찾기
def find_root(root, x):
    if root[x] != x:
        root[x] = find_root(root, root[x])
    return root[x]


# 두 노드가 속한 집합 합치기
def union_root(root, x, y):
    x = find_root(root, x)
    y = find_root(root, y)
    if x < y:
        root[y] = x
    else:
        root[x] = y


N, M = map(int, input().split())
parent = [0] * (N + 1)

# 부모 테이블 초기화
for i in range(N + 1):
    parent[i] = i

# 간선 정보 입력
edge = []
cost = 0

for __ in range(M):
    A, B, C = map(int, input().split())
    edge.append((C, A, B))

# 오름차순으로 정렬
edge.sort()
biggest = 0  # 최소 신장 트리에서 가장 큰 간선을 제거해야 2개로 분리 가능

for c, a, b in edge:
    # 사이클이 존재하지 않을때만 수행
    if find_root(parent, a) != find_root(parent, b):
        union_root(parent, a, b)
        cost += c
        biggest = c

print(cost - biggest)
