def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y = build[0], build[1]
        building = build[2]
        if build[3] == 1:
            answer.append([x, y, building])
            if not possible(answer):
                answer.remove([x, y, building])
        else:
            answer.remove([x, y, building])
            if not possible(answer):
                answer.append([x, y, building])
    return sorted(answer)


def possible(blueprint):
    for x, y, building in blueprint:
        if building == 0:
            if y == 0 or [x, y - 1, 0] in blueprint or [x, y, 1] in blueprint or [x - 1, y, 1] in blueprint:
                continue
            else:
                return False
        else:
            if [x, y - 1, 0] in blueprint or [x + 1, y - 1, 0] in blueprint or (
                    [x + 1, y, 1] in blueprint and [x - 1, y, 1] in blueprint):
                continue
            else:
                return False
    return True


tn = 5
tbf = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
       [1, 1, 1, 0], [2, 2, 0, 1]]

print(solution(tn, tbf))
