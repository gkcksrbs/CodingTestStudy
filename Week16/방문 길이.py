def solution(dirs):
    answer = 0
    now = (0, 0)
    last = (0, 0)
    visited = []
    for i in dirs:
        if i == 'U':
            if now[0] == 5:
                continue
            last = now
            now = (now[0]+1, now[1])
        elif i == 'D':
            if now[0] == -5:
                continue
            last = now
            now = (now[0]-1, now[1])
        elif i == 'L':
            if now[1] == -5:
                continue
            last = now
            now = (now[0], now[1]-1)
        else:
            if now[1] == 5:
                continue
            last = now
            now = (now[0], now[1]+1)
        if [last, now] not in visited and [now, last] not in visited:
            answer += 1
            visited.append([last, now])
    return answer


if __name__ == '__main__':
    print(solution("ULURRDLLU"))
    print(solution("LULLLLLLU"))
    print(solution("RL"))