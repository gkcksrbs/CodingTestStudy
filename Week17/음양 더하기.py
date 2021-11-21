# 프로그래머스: 월간 코드 챌린지 시즌2 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


if __name__ == '__main__':
    print(solution([4, 7, 12], [True, False, True]))
