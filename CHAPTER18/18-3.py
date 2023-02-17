# Q43 어두운 길
# 최소 신장 트리 - 크루스칼 알고리즘

N, M = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


parents = [*range(N + 1)]
road = []
result = 0

for __ in range(M):
    X, Y, Z = map(int, input().split())
    road.append((Z, X, Y))
    result += Z

road.sort()

for cost, a, b in road:
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        result -= cost

print(result)
