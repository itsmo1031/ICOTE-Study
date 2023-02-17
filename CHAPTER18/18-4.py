# Q44 행성 터널
# Link: https://www.acmicpc.net/problem/2887

N = int(input())


def find_parent(parent, k):
    if parent[k] != k:
        parent[k] = find_parent(parent, parent[k])
    return parent[k]


def union_parent(parent, k, j):
    k = find_parent(parent, k)
    j = find_parent(parent, j)
    if k < j:
        parent[j] = k
    else:
        parent[k] = j


parents = [*range(N + 1)]
x = []
y = []
z = []

for i in range(1, N + 1):
    X, Y, Z = map(int, input().split())
    x.append((X, i))
    y.append((Y, i))
    z.append((Z, i))

x.sort()
y.sort()
z.sort()

edges = []

for i in range(N - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()
result = 0

for cost, a, b in edges:
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        result += cost

print(result)
