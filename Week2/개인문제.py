def dfs(lst, res, target):
    if not lst:
        if res == target:
            return 1
        else:
            return 0
    return dfs(lst[1:], res+lst[0], target) + dfs(lst[1:], res-lst[0], target)
def solution(numbers, target):
    answer = dfs(numbers, 0, target)
    return answer

print(solution([1, 1, 1, 1, 1], 3))