# 코딩테스트 연습 스택/큐 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque


def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    speeds_q = deque(speeds)

    while q:
        for i in range(len(speeds_q)):
            q[i] += speeds_q[i]

        if q[0] >= 100:
            count = 0
            while True:
                if q:
                    if q[0] < 100:
                        break
                    q.popleft()
                    speeds_q.popleft()
                    count += 1
                else:
                    break
            answer.append(count)

    return answer


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
