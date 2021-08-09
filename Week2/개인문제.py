# 프로그래머스 고득점 Kit: 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

# 깊이 우선 탐색 알고리즘
def dfs(lst, res, target):
    # lst 에 원소가 없을 떄
    if not lst:
        # target 값과 같은 결과가 나오면 1 반환, 나오지 않으면 0 반환
        if res == target:
            return 1
        else:
            return 0
    # 재귀 함수
    return dfs(lst[1:], res+lst[0], target) + dfs(lst[1:], res-lst[0], target)


def solution(numbers, target):
    # 깊이 우선 탐색 알고리즘 실행
    answer = dfs(numbers, 0, target)
    # 결과값 반환
    return answer


# test code
print(solution([1, 1, 1, 1, 1], 3))