# 코딩테스트 연습 Summer/Winter Coding(2019) 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048
from math import gcd


def solution(w, h):
    return w*h - (w+h-gcd(w, h))


if __name__ == '__main__':
    print(solution(100000000, 99999999))