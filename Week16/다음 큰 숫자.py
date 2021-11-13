# 프로그래머스: 연습문제 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911
from collections import Counter


def solution(n):
    counter = Counter(bin(n)[2:])
    num = n+1
    while True:
        tmp = Counter((bin(num)[2:]))
        if counter['1'] == tmp['1']:
            answer = num
            break
        num += 1
    return answer
