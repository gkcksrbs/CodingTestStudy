# 프로그래머스 월간 코드 챌린지 시즌3 공 이동 시뮬레이션
# https://programmers.co.kr/learn/courses/30/lessons/87391
def solution(n, m, x, y, queries):
    answer = -1
    moveX, moveY = [], []
    rangeX = [x, x]
    rangeY = [y, y]
    # for query in queries:
    #     if query[0] == 2 or query[0] == 3:
    #         if query[0] == 2:
    #             moveX.append(-query[1])
    #         else:
    #             moveX.append(query[1])
    #     else:
    #         if query[0] == 0:
    #             moveY.append(-query[1])
    #         else:
    #             moveY.append(query[1])
    for i in range(len(queries)-1, -1, -1):
        if queries[i][0] == 2 or queries[i][0] == 3:
            if queries[i][0] == 2:
                if range
                rangeX[0] += queries[i][1]
                rangeX[1] += queries[i][1]

    print(rangeX)
    # print(moveX)
    # print(moveY)
    return answer


if __name__ == '__main__':
    # print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
    print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))
    # print(solution(10e9, 10e9, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
