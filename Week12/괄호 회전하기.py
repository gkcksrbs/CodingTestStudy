# 프로그래머스: 월간 코드 챌린지 시즌2 괄호 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/76502
from collections import deque


def solution(s):
    answer = 0
    if len(s) == 1 or len(s) % 2 == 1:
        return answer
    q = deque(s)
    for i in range(len(q)):
        stack = []
        for j in q:
            if j == '{' or j == '[' or j == '(':
                stack.append(j)
            else:
                if stack:
                    if j == '}' and stack[-1] == '{':
                        stack.pop()
                    elif j == ']' and stack[-1] == '[':
                        stack.pop()
                    elif j == ')' and stack[-1] == '(':
                        stack.pop()
        if len(stack) == 0:
            answer += 1
        first = q.popleft()
        q.append(first)
    return answer



if __name__ == '__main__':
    print(solution("[](){}"))
    print(solution("}]()[{"))
    print(solution("[]{"))
    print(solution("}}}"))
    print(solution("}}}}"))