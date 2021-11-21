from itertools import combinations


def solution(nums):
    answer = 0

    for num in combinations(nums, 3):
        tmp = num[0] + num[1] + num[2]
        is_prime = True
        for i in range(2, int(tmp**0.5)+1):
            if tmp % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 4]))
