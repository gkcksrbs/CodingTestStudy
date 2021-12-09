# 프로그래머스: 연습문제 짝수와 홀수
# https://programmers.co.kr/learn/courses/30/lessons/12937
def solution(num):
    if num % 2 == 0:
        return 'Even'
    return 'Odd'


if __name__ == '__main__':
    print(solution(3))
