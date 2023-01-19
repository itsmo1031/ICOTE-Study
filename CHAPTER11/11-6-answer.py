import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_times = 0
    prev = 0
    length = len(food_times)

    while sum_times + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0]  # 해치울 음식의 시간값
        sum_times += (now - prev) * length
        length -= 1
        prev = now

    result = sorted(q, key=lambda x: x[1])

    answer = result[(k - sum_times) % length][1]
    return answer


print(solution([3, 1, 2], 5))
