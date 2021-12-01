# 프로그래머스: 연습문제 최솟값 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12941
def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer


if __name__ == '__main__':
    print(solution([1, 4, 2], [5, 4, 4]))
