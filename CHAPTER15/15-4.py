# Q30 가사 검색
# Link: https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right


def count(arr, v_from, v_to):
    return bisect_right(arr, v_to) - bisect_left(arr, v_from)


def solution(words, queries):
    answer = []
    # 모든 가사를 단어 수로 분류하여 저장하기 위해 리스트 선언
    words_by_len = [[] for __ in range(10001)]
    # 와일드카드가 접두사로 주어졌을 경우 뒤쪽부터 검색하기 위한 리스트 선언
    reversed_words_by_len = [[] for __ in range(10001)]

    # 글자 수에 따라 나눠서 각 단어 저장. 반대 검색을 위해 뒤집어진 문자열도 저장. 이후 자리수 맞춰서 정렬
    for w in words:
        words_by_len[len(w)].append(w)
        reversed_words_by_len[len(w)].append(w[::-1])
    for i in range(10001):
        words_by_len[i].sort()
        reversed_words_by_len[i].sort()

    for q in queries:
        # 쿼리의 와일드카드가 뒤쪽에 주어졌을 경우 순차 검색, 앞쪽에 주어졌을 경우 반대로 검색
        if q[0] != '?':
            result = count(words_by_len[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            result = count(reversed_words_by_len[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 결과값 answer에 저장
        answer.append(result)

    return answer


tw = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
tq = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(tw, tq))
