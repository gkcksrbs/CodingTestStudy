# 프로그래머스: Summer/Winter Coding(~2018) 점프와 순간 이동
# https://programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 0
    while n != 1:
        if n % 2 == 1:
            ans += 1
        n = n // 2
    return ans + 1


if __name__ == '__main__':
    print(solution(5000))
