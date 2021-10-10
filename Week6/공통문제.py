# 코딩테스트 연습 2020 카카오 인턴십 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257#
from itertools import permutations

def solution(expression):
    lst = list(expression)
    data = []
    num = ''
    using = []
    result = []
    while lst:
        now = lst.pop(0)
        if now == '*' or now == '-' or now == '+':
            data.append(int(num))
            data.append(now)
            num = ''
            if now not in using:
                using.append(now)
        else:
            num += now
    data.append(int(num))

    for cond in permutations(using):
        cond = list(cond)
        copied = data.copy()
        while cond:
            val = cond.pop(0)
            while val in copied:
                index = copied.index(val)
                if val == '-':
                    temp = copied[index - 1] - copied[index + 1]
                elif val == '+':
                    temp = copied[index - 1] + copied[index + 1]
                else:
                    temp = copied[index - 1] * copied[index + 1]
                copied[index] = temp
                copied.pop(index - 1)
                copied.pop(index)
        result.append(abs(copied[-1]))

    return max(result)


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
