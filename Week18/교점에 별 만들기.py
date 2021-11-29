# 프로그래머스: 위클리 챌린지 교점에 별 만들기
# https://programmers.co.kr/learn/courses/30/lessons/87377
from itertools import combinations


def solution(line):
    answer = []
    meet = []
    range_x, range_y = [0, 0], [0, 0]
    for A, B in combinations(line, 2):
        a, b, e = A[0], A[1], A[2]
        c, d, f = B[0], B[1], B[2]
        if a*d - b*c == 0:
            continue
        x = (b*f - e*d) / (a*d - b*c)
        y = (e*c - a*f) / (a*d - b*c)
        if x % 1 == 0.0 and y % 1 == 0.0:
            meet.append([int(y), int(x)])
    meet.sort()
    range_y[0], range_y[1] = meet[0][0], meet[-1][0]
    meet.sort(key=lambda t: t[1])
    range_x[0], range_x[1] = meet[0][1], meet[-1][1]
    for m in meet:
        m[0], m[1] = m[0] - range_y[0], m[1] - range_x[0]
    range_x[0], range_x[1] = range_x[0] - range_x[0], range_x[1] - range_x[0]
    range_y[0], range_y[1] = range_y[0] - range_y[0], range_y[1] - range_y[0]
    graph = []
    for i in range(range_y[1]+1):
        tmp = ['.']*(range_x[1]+1)
        for j in range(range_x[1]+1):
            if [i, j] in meet:
                tmp[j] = '*'
        graph.insert(0, tmp)
    for i in graph:
        answer.append(''.join(i))
    return answer


if __name__ == '__main__':
    print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
