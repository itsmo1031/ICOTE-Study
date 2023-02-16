# Q42 탑승구

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


G = int(input())
P = int(input())
parents = [*range(G + 1)]

for i in range(P):
    plane_parent = find_parent(parents, int(input()))
    if plane_parent == 0:
        print(i)
        break
    union_parent(parents, plane_parent, plane_parent - 1)
