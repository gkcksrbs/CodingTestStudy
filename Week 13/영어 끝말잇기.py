# 프로그래머스: Summer/Winter Coding(~2018) 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = [0, 0]
    record = [words[0]]
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in record:
            if (i+1) % n == 0:
                answer[0] = n
            else:
                answer[0] = (i+1) % n
            answer[1] = i // n + 1
            break
        else:
            record.append(words[i])

    return answer


if __name__ == '__main__':
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
    print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish",
                       "hang", "gather", "refer", "reference", "estimate", "executive"]))
    print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "e", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
