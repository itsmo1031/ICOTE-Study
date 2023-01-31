# Q25 싪패율
# Link: https://programmers.co.kr/learn/courses/30/lessons/42889

ex_N = 3
ex_stages = [1, 1, 1]


def solution(N, stages: list):
    # 스테이지별 실패율 담을 리스트 선언
    failure = []

    # 각 단계별로 수행
    for i in range(N):
        # 현재 스테이지 이상으로 접근한 유저 추리기
        current = [x for x in stages if x >= i + 1]
        # 현재 스테이지에 도달한 유저가 없을 경우 실패율은 0
        f = 0
        if current:
            # 도달한 유저가 있을 경우 실패율 계산
            f = current.count(i + 1) / len(current)
        # (현재 단계, 실패율)을 담은 튜플을 실패율 리스트에 추가
        failure.append((i + 1, f))

    # 실패율 내림차순으로 리스트 정렬
    failure.sort(key=lambda x: x[1], reverse=True)

    # 정렬된 리스트에서 이름만 출력
    # answer = [x[0] for x in failure]
    answer = [*[*zip(*failure)][0]]
    return answer


print(solution(ex_N, ex_stages))
