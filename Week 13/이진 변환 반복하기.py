# 프로그래머스: 월간 코드 챌린지 시즌1 이진 변환 반복하기
# https://programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    answer = [0, 0]
    while s != '1':
        last = len(s)
        s = s.replace('0', '')
        answer[1] += last - len(s)
        s = bin(len(s))[2:]
        answer[0] += 1
    return answer


if __name__ == '__main__':
    print(solution("110010101001"))