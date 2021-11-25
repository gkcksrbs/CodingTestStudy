# 프로그래머스: 연습문제 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    secret = '*' * (len(phone_number) - 4)
    return secret + phone_number[-4:]


if __name__ == '__main__':
    print(solution("01033334444"))
