# 프로그래머스 월간 코드 챌린지 시즌3 공 이동 시뮬레이션
# https://programmers.co.kr/learn/courses/30/lessons/87391
rangeX = []


def solution(n, m, x, y, queries):
    global rangeX
    answer = -1
    rangeX = [x, x]
    rangeY = [y, y]
    print(rangeX)
    for i in range(len(queries)-1, -1, -1):
        if queries[i][0] == 2 or queries[i][0] == 3:
            if queries[i][0] == 2:
                if rangeX[0] != 0:
                    rangeX[0] += queries[i][1]
                if rangeX[1] + queries[i][1] > n:
                    rangeX[1] = n-1
                else:
                    rangeX[1] += queries[i][1]
            else:
                if rangeX[1] != n-1:
                    rangeX[1] -= queries[i][1]
                if rangeX[0] - queries[i][1] < 0:
                    rangeX[0] = 0
                else:
                    rangeX[0] -= queries[i][1]
        else:
            if rangeY[1] != m-1:
                rangeY[1] += queries[i][1]
            if rangeY[0] + queries[i][1] > m:

            print(rangeX)

    # ud = []
    # lr = []
    # for query in queries:
    #     if query[0] == 2 or query[0] == 3:
    #         ud.append(query)
    #     else:
    #         lr.append(query)
    #
    # print(ud)
    # print(lr)
    return answer


# def up_down(query):
#     if query[0] == 2:
#         if rangeX[0] != 0:
#             rangeX[0] += query[1]
#         if rangeX[1] + query[1] > n
#     return


if __name__ == '__main__':
    # print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
    print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))
    # print(solution(10e9, 10e9, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
