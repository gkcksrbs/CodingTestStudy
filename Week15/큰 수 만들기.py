# 프로그래머스: 탐욕법(Greedy) 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883
# def solution(number, k):
#     answer = ''
#     number = list(number)
#     if k == 1:
#         number.remove(min(number))
#         return ''.join(number)
#     while k != 0:
#         max_idx = number.index(max(number[:k+1]))
#         if max_idx != 0:
#             for i in range(max_idx):
#                 del number[0]
#         else:
#             answer += number[0]
#             del number[0]
#         k -= max_idx
#     return answer + ''.join(number)

def solution(number, k):
    answer = []
    for num in number:
        if not answer:
            answer.append(num)
        else:
            if k > 0:
                while answer[-1] < num:
                    answer.pop()
                    k -= 1
                    if not answer or k <= 0:
                        break
            answer.append(num)
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)


if __name__ == '__main__':
    print(solution("1924", 2))
    print(solution("1231234", 3))
    print(solution("4177252841", 4))
    print(solution("77777", 1))
