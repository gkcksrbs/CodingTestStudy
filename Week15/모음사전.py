# 프로그래머스: 위클리 챌린지 모음사전
# https://programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product


def solution(word):
    answer = 0
    data = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(1, 6):
        tmp = list(product(data, repeat=i))
        for j in tmp:
            dictionary.append(''.join(j))
    dictionary.sort()
    answer = dictionary.index(word) + 1
    return answer


if __name__ == '__main__':
    print(solution("AAAAE"))
    print(solution("AA"))
