# 프로그래머스: 스택/큐 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    answer = 1
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    while q:
        if len(q) == 1:
            return len(priorities)
        now = q.popleft()
        max_num = max(q)[0]
        if now[0] >= max_num:
            if now[1] == location:
                break
            answer += 1
        else:
            q.append(now)

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 9, 1, 1, 1], 0))
    print(solution([2, 1, 3, 2], 2))