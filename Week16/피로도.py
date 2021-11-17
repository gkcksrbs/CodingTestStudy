# 프로그래머스: 위클리 챌린지 피로도
# https://programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    answer = -1
    idx = [i for i in range(len(dungeons))]
    for lst in permutations(idx, len(idx)):
        tired = k
        lst = list(lst)
        count = 0
        for i in lst:
            if dungeons[i][0] <= tired:
                tired -= dungeons[i][1]
                count += 1
        answer = max(answer, count)
    return answer


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))
