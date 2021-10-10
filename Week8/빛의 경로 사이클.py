# 코딩테스트 연습 월간 코드 챌린지 시즌3 빛의 경로 사이클
# https://programmers.co.kr/learn/courses/30/lessons/86052
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def solution(grid):
    answer = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                length = 0
                point = (i, j)
                now = k
                path_set = set()
                while True:
                    prev_point = point
                    point = (point[0]+direction[now][0], point[1]+direction[now][1])
                    path = (prev_point, point)
                    if path in path_set:
                        break
                    else:
                        path_set.add(path)
                        length += 1
                    if point[0] >= len(grid):
                        point = (0, point[1])
                    elif point[1] >= len(grid[0]):
                        point = (point[0], 0)
                    elif point[0] < 0:
                        point = (len(grid)-1, point[1])
                    elif point[1] < 0:
                        point = (point[0], len(grid[0])-1)
                    if grid[point[0]][point[1]] == 'R':
                        now = (now+1) % 4
                    elif grid[point[0]][point[1]] == 'L':
                        now = (now+3) % 4
                if length:
                    answer.append(length)
    return sorted(answer)


print(solution(["SL", "LR"]))
print(solution(["S"]))
print(solution(["R", "R"]))