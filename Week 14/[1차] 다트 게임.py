# 프로그래머스: 2018 KAKAO BLIND RECRUITMENT [1차] 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    score = [0, 0, 0]
    index = 0
    idx = 0
    for i in dartResult:
        if i.isnumeric():
            if i == '0' and dartResult[idx-1] == '1':
                score[index] = 10
            else:
                score[index] = int(i)
        elif i == 'S':
            score[index] = score[index] ** 1
            if idx+1 < len(dartResult):
                if dartResult[idx+1] != '*' and dartResult[idx+1] != '#':
                    index += 1
        elif i == 'D':
            score[index] = score[index] ** 2
            if idx + 1 < len(dartResult):
                if dartResult[idx + 1] != '*' and dartResult[idx + 1] != '#':
                    index += 1
        elif i == 'T':
            score[index] = score[index] ** 3
            if idx + 1 < len(dartResult):
                if dartResult[idx + 1] != '*' and dartResult[idx + 1] != '#':
                    index += 1
        elif i == '*':
            score[index] *= 2
            if index != 0:
                score[index-1] *= 2
            index += 1
        elif i == '#':
            score[index] *= -1
            index += 1
        idx += 1
    return sum(score)


if __name__ == '__main__':
    print(solution('1S2D*3T'))
    print(solution('1D2S#10S'))