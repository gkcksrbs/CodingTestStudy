# 월간 코드 챌린지 시즌1 : 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644
from itertools import combinations


def solution(numbers):
    answer = []
    # 조합을 이용해서 2개의 숫자를 뽑고 더한 값을 answer 배열에 저장
    for i in combinations(numbers, 2):
        answer.append(sum(i))
    # 중복값 제거
    answer = list(set(answer))
    # 정렬 후 결과값 반환
    return sorted(answer)


# test code
print(solution([5,0,2,7]))
