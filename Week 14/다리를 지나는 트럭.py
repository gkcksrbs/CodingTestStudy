# 프로그래머스: 스택/큐 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridge_weight = 0
    while bridge:
        answer += 1
        bridge_weight -= bridge.pop(0)
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                tmp = truck_weights.pop(0)
                bridge.append(tmp)
                bridge_weight += tmp
            else:
                bridge.append(0)
    return answer


if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))
