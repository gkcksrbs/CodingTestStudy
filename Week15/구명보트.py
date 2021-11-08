# 프로그래머스: 탐욕법(Greedy) 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people)-1
    while left <= right:
        answer += 1
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
    return answer


if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))
    print(solution([70, 50, 80, 50], 130))
    print(solution([40, 40, 60, 70, 80], 160))