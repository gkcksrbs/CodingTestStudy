# 프로그래머스: 탐욕법(Greedy) 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    change = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0:
            break
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer


if __name__ == '__main__':
    print(solution("JEROEN"))
    print(solution("JAN"))
    print(solution("ZZAAAZZ"))
