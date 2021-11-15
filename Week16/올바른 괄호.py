from collections import deque


def solution(s):
    stack = deque()
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.popleft()
    if stack:
        return False
    else:
        return True


if __name__ == '__main__':
    print(solution("()()"))
    print(solution(")()("))