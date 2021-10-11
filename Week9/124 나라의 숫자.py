# 코딩테스트 연습 연습문제 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    while n > 3:
        if n % 3 == 0:
            answer = '4' + answer
            n = n//3 - 1
        else:
            answer = str(n % 3) + answer
            n = n // 3
    if n == 3:
        answer = '4' + answer
    else:
        answer = str(n) + answer
    return answer


if __name__ == '__main__':
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(6))
    print(solution(7))
    print(solution(8))
    print(solution(9))
    print(solution(10))


