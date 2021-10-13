# 2021 KAKAO BLIND RECRUITMENT 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        lst = []
        for order in orders:
            order = sorted(order)
            for comb in combinations(order, i):
                lst.append(''.join(comb))
        cnt = Counter(lst)
        result = cnt.most_common()
        if not result:
            break
        else:
            max_num = result[0][1]
            for res in result:
                if res[1] == max_num and max_num >= 2:
                    answer.append(res[0])
    return sorted(answer)


if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
