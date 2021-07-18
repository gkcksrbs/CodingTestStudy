# 2020 카카오 인턴십 기출문제 1 - 키패트 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

# 각 키패드의 location 저장 dictionary
key_loc = {1: (1, 1), 2: (1, 2), 3: (1, 3), 4: (2, 1), 5: (2, 2),
           6: (2, 3), 7: (3, 1), 8: (3, 2), 9: (3, 3), 0: (4, 2), '*': (4, 1), '#': (4, 3)}


def solution(numbers, hand):
    answer = ''
    left_loc = '*'            # 왼쪽 엄지 손가락의 현재 위치
    right_loc = '#'           # 오른쪽 엄지손가락 의 현재 위치

    for i in numbers:         # 입력할 번호 순차 탐색

        if i in [1, 4, 7]:    # 1, 4, 7일 경우 왼쪽 손가락으로 누르기, 현재 왼쪽 엄지 손가락 위치 변경
            answer += 'L'
            left_loc = i
        elif i in [3, 6, 9]:  # 3, 6, 9일 경우 오른쪽 엄지 손가락으로 누르기, 현재 오른쪽 손가락 위치 변경
            answer += 'R'
            right_loc = i
        else:                 # 2, 5, 8, 0일 경우
            # 왼쪽 엄지손가락의 위치와 다음 입력할 키패드 사이의 거리 / 오른쪽 엄지손가락의 위치와 다음 입력할 키패드 사이의 거리 비교
            if distance(left_loc, i) < distance(right_loc, i):      # 왼쪽 엄지 손가락이 다음 입력할 키와 더 가까울 경우
                answer += 'L'     # 왼쪽 엄지 손가락으로 누르기
                left_loc = i      # 현재 왼쪽 엄지 손가락 위치 변경
            elif distance(left_loc, i) > distance(right_loc, i):    # 오른쪽 엄지 손가락이 다음 입력할 키와 더 가까울 경우
                answer += 'R'     # 오른쪽 엄지 손가락으로 누르기
                right_loc = i     # 현재 오른쪽 엄지 손가락 위치 변경
            else:                                                   # 두 엄지 손가락이 다음 입력할 키와 거리가 같을 경우
                # 오른손잡이
                if hand == 'right':
                    answer += 'R'
                    right_loc = i
                # 왼손 잡이
                else:
                    answer += 'L'
                    left_loc = i
    # 결과값 반환
    return answer


# 두 키패드 사이의 거리를 반환해주는 함수
def distance(key1, key2):
    return abs(key_loc[key1][0] - key_loc[key2][0]) + abs(key_loc[key1][1] - key_loc[key2][1])


# test
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
