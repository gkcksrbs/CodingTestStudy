# 프로그래머스 고득점 Kit: 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter


def solution(participant, completion):
    # 참가자 리스트, 완주 선수 리스트를 합친 후 Counter 로 생성
    answer = Counter(participant + completion)
    # 해당 이름의 key 값이 홀수면 완주 못한 사람이므로 결과 반환
    for i in answer:
        if not answer[i] % 2 == 0:
            return i


# test code
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))