# 팀 결성

# 루트 노드 찾기
def find_root(root, x):
    if root[x] != x:
        root[x] = find_root(root, root[x])
    return root[x]


# 루트 노드 합치기
def union_root(root, x, y):
    x = find_root(root, x)
    y = find_root(root, y)
    if x < y:
        root[y] = x
    else:
        root[x] = y


N, M = map(int, input().split())
parent = [0] * (N + 1)

# 부모 노드 자기 자신으로 초기화
for i in range(N + 1):
    parent[i] = i

for i in range(M):
    op, a, b = map(int, input().split())
    # 합집합 연산일 경우
    if op == 0:
        union_root(parent, a, b)
    # 같은팀 찾기 연산일 경우
    elif op == 1:
        if find_root(parent, a) == find_root(parent, b):
            print("YES")
        else:
            print("NO")
