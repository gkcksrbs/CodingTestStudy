# 프로그래머스: 월간 코드 챌린지 시즌1 쿼드압축 후 개수 세기
# https://programmers.co.kr/learn/courses/30/lessons/68936
def solution(arr):
    answer = [0, 0]
    array = []
    for i in arr:
        array += i
    array = divide_conquer(array)
    for i in array:
        if i == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer


def divide_conquer(arr):
    if len(arr) == 1:
        return arr
    if 0 not in arr or 1 not in arr:
        return list(set(arr))
    length = int(len(arr) ** 0.5)
    left_up = []
    left_down = []
    right_up = []
    right_down = []
    for i in range(len(arr)):
        row = i // length
        col = i % length
        if row < length // 2 and col < length // 2:
            left_up.append(arr[i])
        elif row < length // 2 <= col:
            right_up.append(arr[i])
        elif row >= length // 2 > col:
            left_down.append(arr[i])
        else:
            right_down.append(arr[i])
    if 0 not in left_up or 1 not in left_up:
        left_up = list(set(left_up))
    else:
        left_up = divide_conquer(left_up)
    if 0 not in right_up or 1 not in right_up:
        right_up = list(set(right_up))
    else:
        right_up = divide_conquer(right_up)
    if 0 not in left_down or 1 not in left_down:
        left_down = list(set(left_down))
    else:
        left_down = divide_conquer(left_down)
    if 0 not in right_down or 1 not in right_down:
        right_down = list(set(right_down))
    else:
        right_down = divide_conquer(right_down)
    return left_up + right_up + left_down + right_down


if __name__ == '__main__':
    print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
    print(solution(
        [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
    print(solution([[0, 0], [0, 0]]))
