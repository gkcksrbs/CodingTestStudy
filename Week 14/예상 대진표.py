# 프로그래머스: 2017 팁스타운 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985
def solution(n, a, b):
    answer = 0
    is_matched = False
    lst = []
    for i in range(1, n+1, 2):
        lst.append([i, i+1])
    while not is_matched:
        answer += 1
        for i in lst:
            if a in i and b in i:
                is_matched = True
                break
        tmp = []
        if len(lst) >= 2:
            for i in range(0, len(lst), 2):
                tmp.append(lst[i]+lst[i+1])
            lst = tmp
    return answer


if __name__ == '__main__':
    print(solution(8, 4, 7))