# 프로그래머스: 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    answer = []
    zero_count = 0
    win_count = 0
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    for lotto in lottos:
        if lotto == 0:
            zero_count += 1
        elif lotto in win_nums:
            win_count += 1
    answer.append(rank[win_count + zero_count])
    answer.append(rank[win_count])
    return answer


if __name__ == '__main__':
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
