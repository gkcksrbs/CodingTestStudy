# 프로그래머스: 2018 KAKAO BLIND RECRUITMENT [1차] 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679
def solution(m, n, board):
    answer = 0
    graph = []
    for i in board:
        graph.append(list(i))
    while True:
        erases = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if graph[i][j] == -1:
                    continue
                if graph[i][j] == graph[i][j + 1] == graph[i + 1][j] == graph[i + 1][j + 1]:
                    erases.add((i, j))
                    erases.add((i, j + 1))
                    erases.add((i + 1, j))
                    erases.add((i + 1, j + 1))
        if not erases:
            break
        for x, y in erases:
            graph[x][y] = -1
        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                x, y = i, j
                while graph[x][y] != -1 and graph[x+1][y] == -1:
                    graph[x][y], graph[x+1][y] = graph[x+1][y], graph[x][y]
                    x += 1
                    if x == m-1:
                        break
    for i in graph:
        for j in i:
            if j == -1:
                answer += 1
    return answer


if __name__ == '__main__':
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
