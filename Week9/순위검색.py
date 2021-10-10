# 코딩테스트 연습 2021 KAKAO BLIND RECRUITMENT 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412
from itertools import combinations
from bisect import bisect_left


def solution(information, query):
    answer = []
    case = {}
    graph = []
    for info in information:
        conditions = info.split()
        for j in range(5):
            for comb in combinations([0, 1, 2, 3], j):
                tmp = ''
                for i in range(4):
                    if i in comb:
                        tmp += '-'
                    else:
                        tmp += conditions[i]
                if tmp not in case.keys():
                    case[tmp] = [int(conditions[-1])]
                else:
                    case[tmp].append(int(conditions[-1]))
    for key in case.keys():
        case[key].sort()
    for q in query:
        tmp = q.split()
        key = tmp[0] + tmp[2] + tmp[4] + tmp[6]
        if key in case.keys():
            answer.append(len(case[key]) - bisect_left(case[key], int(tmp[-1])))
        else:
            answer.append(0)
    return answer


print(
    solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"])
)
