# 프로그래머스: 연습문제 문자열을 정수로 바꾸기
# https://programmers.co.kr/learn/courses/30/lessons/12925
def solution(s):
    if s[0] == '-':
        return -int(s[1:])
    return int(s)


if __name__ == '__main__':
    print(solution("-1234"))