# 2018 KAKAO BLIND RECRUITMENT [1차] 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677
from collections import Counter


def solution(str1, str2):
    lst_str1, lst_str2 = [], []

    str1, str2 = str1.lower(), str2.lower()

    for i in range(len(str1)-1):
        s = str1[i:i+2]
        if s.isalpha():
            lst_str1.append(s)

    for i in range(len(str2)-1):
        s = str2[i:i+2]
        if s.isalpha():
            lst_str2.append(s)

    lst_str1, lst_str2 = Counter(lst_str1), Counter(lst_str2)

    if not lst_str1 and not lst_str2:
        return 65536

    union = lst_str1 | lst_str2
    intersection = lst_str1 & lst_str2

    return int(sum(intersection.values())/sum(union.values())*65536)


if __name__ == "__main__":
    print(solution("FRANCE", "french"))
    print(solution("aa1+aa2", "AAAA12"))
    print(solution("E=M*C^2", "e=m*c^2"))