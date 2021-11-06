# 프로그래머스: 해시 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        if cloth[1] not in dic.keys():
            dic[cloth[1]] = 1
        else:
            dic[cloth[1]] += 1
    for val in dic.values():
        answer *= (val+1)
    return answer-1


if __name__ == '__main__':
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))