# 코딩테스트 연습 힙(Heap) 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        if len(scoville) <= 1 and scoville[0] <= K:
            return -1
        min_hot = heapq.heappop(scoville)
        if min_hot >= K:
            break
        second_min_hot = heapq.heappop(scoville)
        heapq.heappush(scoville, min_hot+second_min_hot*2)
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))
    print(solution([1, 1, 100], 7))