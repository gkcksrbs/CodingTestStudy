from collections import Counter


def solution(participant, completion):
    answer = Counter(participant + completion)
    for i in answer:
        if not answer[i] % 2 == 0:
            return i


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))