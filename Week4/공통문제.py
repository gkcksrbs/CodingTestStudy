from itertools import combinations

def solution(numbers):
    answer = []

    for i in combinations(numbers, 2):
        answer.append(sum(i))

    answer = list(set(answer))
    return sorted(answer)

print(solution([5,0,2,7]))
