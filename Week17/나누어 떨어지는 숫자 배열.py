# 프로그래머스: 연습문제 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if not answer:
        answer.append(-1)
    return sorted(answer)


if __name__ == '__main__':
    print(solution([5, 9, 7, 10], 5))
    print(solution([3, 2, 6], 10))
