# 프로그래머스 고득점 Kit: 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    # 여별을 갖고 온 학생 중 도난 당한 학생 제거, 도난 당한 학생 중 여벌을 갖고 온 학생 제거
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    # 여벌을 갖고 온 학생들에서 양 옆 학생중 한명이 도난 당했다면 빌려주고 set_lost 배열에서 도난 당한 학생 제거
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    # 결과값 반환
    return n-len(set_lost)


# test code
print(solution(3, [3], [1]))