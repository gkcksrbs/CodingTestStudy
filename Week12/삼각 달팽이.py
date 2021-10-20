# 프로그래머스: 월간 코드 챌린지 시즌1 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    answer = []
    graph = []
    move = [(1, 0), (0, 1), (-1, -1)]
    for i in range(n):
        graph.append([-1]*(i+1))
    num = 0
    for i in range(1, n+1):
        num += i
    now = [0, 0]
    count = 1
    index = 0
    while count <= num:
        graph[now[0]][now[1]] = count
        if (now[0] + move[index][0] >= n and index == 0) or (now[1] + move[index][1] > now[0] and index == 1):
            index = (index + 1) % 3
        elif graph[now[0] + move[index][0]][now[1] + move[index][1]] != -1:
            index = (index + 1) % 3
        now[0] += move[index][0]
        now[1] += move[index][1]
        count += 1
    for i in graph:
        for j in i:
            answer.append(j)
    return answer


if __name__ == '__main__':
    print(solution(4))
