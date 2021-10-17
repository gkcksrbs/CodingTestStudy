# 프로그래머스: JadenCase 문자열 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    answer = ''
    temp = s.lower()
    lst = temp.split(' ')

    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()

    answer = ' '.join(lst)

    return answer
