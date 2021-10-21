# 프로그래머스: 월간 코드 챌린지 시즌2 2개 이하로 다른 비트
# https://programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    answer = []
    for number in numbers:
        binary = bin(number)[2:]
        if number % 2 == 0:
            answer.append(number+1)
        else:
            if binary[-2:] == '10':
                answer.append(number+1)
            else:
                count = 0
                for i in range(len(binary)-1, -1, -1):
                    if binary[i] == '0':
                        break
                    count += 1
                answer.append(number+(2**(count-1)))
    return answer


if __name__ == '__main__':
    print(solution([2, 7, 6, 1]))

