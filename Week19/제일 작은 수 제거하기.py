# 프로그래머스: 연습문제 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    arr.remove(min(arr))
    if not arr:
        return [-1]
    return arr


if __name__ == '__main__':
    print(solution([4, 3, 2, 1]))
