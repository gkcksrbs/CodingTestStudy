# 프로그래머스: 연습문제 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940
import math


def solution(n, m):
    answer = [math.gcd(n, m), n*m//math.gcd(n,m)]
    return answer


if __name__ == '__main__':
    print(solution(2, 5))
