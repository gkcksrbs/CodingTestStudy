# 코딩테스트 연습 2021 Dev-Matching: 웹 백엔드 개발자(상반기) 행렬 테두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    answer = []
    graph = []
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx = 0

    for i in range(rows):
        tmp = []
        for j in range(1, columns+1):
            tmp.append(i*columns+j)
        graph.append(tmp)

    for query in queries:
        left_up = (query[0]-1, query[1]-1)
        left_down = (query[2]-1, query[1]-1)
        right_up = (query[0]-1, query[3]-1)
        right_down = (query[2]-1, query[3]-1)
        rotation_check = [left_up, left_down, right_down, right_up]
        now = (query[0]-1, query[1]-1)
        last_num = graph[now[0]][now[1]]
        min_num = graph[now[0]][now[1]]

        for _ in range((right_down[0]-left_up[0] + right_down[1]-left_up[1])*2):
            now = (now[0]+direction[idx][0], now[1]+direction[idx][1])
            min_num = min(min_num, graph[now[0]][now[1]])
            graph[now[0]][now[1]], last_num = last_num, graph[now[0]][now[1]]
            if now in rotation_check:
                idx += 1
        idx = 0

        answer.append(min_num)
    return answer


if __name__ == '__main__':
    print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
    print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
    print(solution(100, 97, [[1, 1, 100, 97]]))