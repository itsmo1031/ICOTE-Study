def solution(food_times, k):
    answer = 0
    idx = 0
    while k > 0:
        if len(set(food_times)) == 1 and list(set(food_times))[0] == 0:
            answer = -1
            return answer
        if food_times[idx] != 0:
            food_times[idx] -= 1
            k -= 1
        if idx + 1 == len(food_times):
            idx = 0
        else:
            idx += 1
    answer = idx + 1
    return answer


print(solution([3, 1, 2], 5))
