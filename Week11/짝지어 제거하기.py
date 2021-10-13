# 2017 팁스타운 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    print(solution("baabaa"))
    print(solution("cdcd"))
