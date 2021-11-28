# 프로그래머스: 스택/큐 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))
