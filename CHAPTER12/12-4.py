def rotate90(m):
    return [*map(list, zip(*m[::-1]))]


def check(m):
    length = len(m) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if m[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    new = [[0] * n * 3 for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new[i + n][j + n] = lock[i][j]

    for _ in range(4):
        key = rotate90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new[x + i][y + j] += key[i][j]
                if check(new):
                    return True
                for i in range(m):
                    for j in range(m):
                        new[x + i][y + j] -= key[i][j]
    return False
