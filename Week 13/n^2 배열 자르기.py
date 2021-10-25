# 프로그래머스: 월간 코드 챌린지 시즌3 n^2 배열 자르기
# https://programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row = i // n
        col = i % n
        answer.append(max(row, col)+1)
    return answer


if __name__ == '__main__':
    print(solution(3, 2, 5))