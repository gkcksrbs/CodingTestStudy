# 프로그래머스: 연습문제 x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

if __name__ == '__main__':
    print(solution(2, 5))
    print(solution(-4, 2))