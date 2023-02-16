# Q41 여행 계획


def find_root(root, x):
    if root[x] != x:
        root[x] = find_root(root, root[x])
    return root[x]


def union_root(root, x, y):
    x = find_root(root, x)
    y = find_root(root, y)
    if x < y:
        root[y] = x
    else:
        root[y] = x


N, M = map(int, input().split())
parent = [*range(N + 1)]

for i in range(N):
    data = [*map(int, input().split())]
    for j in range(N):
        if data[j] == 1:
            union_root(parent, i + 1, j + 1)

plan = [*map(int, input().split())]

if len({map(lambda x: find_root(parent, x), plan)}) == 1:
    print("YES")
else:
    print("NO")
