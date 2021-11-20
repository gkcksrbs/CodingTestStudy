# 프로그래머스: 월간 코드 챌린지 시즌1 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
