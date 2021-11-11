# 프로그래머스: 정렬 H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    answer = 0
    citations.sort()
    left = 0
    right = citations[-1]
    while left <= right:
        up = 0
        down = 0
        mid = (left + right) // 2
        for citation in citations:
            if citation >= mid:
                up += 1
            else:
                down += 1
        if up < mid:
            right = mid - 1
        elif up >= mid:
            left = mid + 1
            answer = mid
        # else:
        #     answer = mid
    return answer


print(solution([3, 0, 6, 1, 5]))
print(solution([22,42]))