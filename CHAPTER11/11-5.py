from collections import Counter
from itertools import combinations

n, m = map(int, input().split())
balls = [*map(int, input().split())]

combi = sum(1 for _ in combinations(balls, 2))  # 볼링공 중 두 가지를 고르는 경우의 수(조합)

dic = Counter(balls)  # 무게가 겹치는 볼링공 개수 체크
sub = 0  # 그 볼링공만큼 빼줘야 하므로 값 설정

for k, v in dic.items():
    if v > 1:
        sub += sum(1 for _ in combinations(range(v), 2))

print(combi - sub)
