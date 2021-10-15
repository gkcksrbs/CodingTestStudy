# 프로그래머스: 연습문제 N개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953
from math import lcm


def solution(arr):
    answer = 1
    for i in arr:
        answer = lcm(answer, i)
    return answer
