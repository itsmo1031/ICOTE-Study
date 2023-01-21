# https://school.programmers.co.kr/learn/courses/30/lessons/60062
# TODO: 한번 더 풀기

from itertools import permutations


def solution(n, weak, dist):
    w_length = len(weak)
    for i in range(w_length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    for start in range(w_length):
        for friends in permutations(dist, len(dist)):
            count = 1
            last_position = weak[start] + friends[count - 1]
            for index in range(start, start + w_length):
                if last_position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    last_position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer


t_n = 12
t_weak = [1, 5, 6, 10]
t_dist = [1, 2, 3, 4]

print(solution(t_n, t_weak, t_dist))
