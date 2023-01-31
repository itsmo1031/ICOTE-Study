# Q26 카드 정렬하기
# Link: https://www.acmicpc.net/problem/1715
import heapq

q = []

for __ in range(int(input())):
    heapq.heappush(q, int(input()))

result = 0

while len(q) != 1:
    add = heapq.heappop(q) + heapq.heappop(q)
    result += add
    heapq.heappush(q, add)

print(result)
