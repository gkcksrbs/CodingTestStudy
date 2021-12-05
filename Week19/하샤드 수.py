# 프로그래머스: 연습문제 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    h = 0
    for i in str(x):
        h += int(i)
    if x % h == 0:
        return True
    return False


if __name__ == '__main__':
    print(solution(11))
