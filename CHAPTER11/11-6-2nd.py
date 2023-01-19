import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    processing_time = 0
    previous = 0

    while processing_time + (q[0][0] - previous) * len(q) <= k:
        now = heapq.heappop(q)[0]
        processing_time += (now - previous) * (len(q) + 1)
        previous = now

    result = sorted(q, key=lambda x: x[1])

    answer = result[(k - processing_time) % len(q)][1]
    return answer


print(solution([3, 1, 2], 5))
