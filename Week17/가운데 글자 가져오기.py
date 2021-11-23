# 프로그래머스: 연습문제 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    if len(s) % 2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    return s[len(s)//2]


if __name__ == '__main__':
    print(solution("abcde"))
    print(solution("qwer"))
