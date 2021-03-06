from collections import deque

visited = []
r, c = 0, 0
NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3


def get_next_step(to, y, x):
    if to == NORTH:
        return y - 1, x
    elif to == SOUTH:
        return y + 1, x
    elif to == WEST:
        return y, x - 1
    else:
        return y, x + 1


def get_next_to(to, ny, nx, grid):
    if to == NORTH:
        if grid[ny][nx] == 'L':
            return WEST
        elif grid[ny][nx] == 'S':
            return NORTH
        elif grid[ny][nx] == 'R':
            return EAST

    elif to == SOUTH:
        if grid[ny][nx] == 'L':
            return EAST
        elif grid[ny][nx] == 'R':
            return WEST
        else:
            return SOUTH

    elif to == EAST:
        if grid[ny][nx] == 'L':
            return NORTH
        elif grid[ny][nx] == 'R':
            return SOUTH
        else:
            return EAST

    else:
        if grid[ny][nx] == 'L':
            return SOUTH
        elif grid[ny][nx] == 'R':
            return NORTH
        else:
            return WEST


def bfs(grid, sy, sx, sto):
    global r, c, visited
    visited[sy][sx][sto] = True
    q = deque()
    cnt = 1
    q.append((sy, sx, sto, cnt))

    while q:
        y, x, to, cnt = q.popleft()
        ny, nx = get_next_step(to, y, x)
        if ny <= -1:
            ny = r - 1
        elif ny >= r:
            ny = 0

        if nx <= -1:
            nx = c - 1
        elif nx >= c:
            nx = 0
        nto = get_next_to(to, ny, nx, grid)

        if visited[ny][nx][nto]: return cnt
        visited[ny][nx][nto] = True
        q.append((ny, nx, nto, cnt + 1))


def solution(grid):
    global visited, r, c
    r = len(grid)
    c = len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(c)] for _ in range(r)]
    answer = []
    for i in range(r):
        for j in range(c):
            for k in (NORTH, SOUTH, EAST, WEST):
                if not visited[i][j][k]: answer.append(bfs(grid, i, j, k))

    answer.sort()
    return answer