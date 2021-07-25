def solution(s):
    answer = []
    test = tuple(map(str, s.split('},')))
    lst = []
    for i in test:
        tmp = i.replace('{', '')
        tmp = tmp.replace('}', '')
        lst.append(set(map(int, tmp.split(','))))
    lst.sort()

    for i in lst:
        if len(i) == 1:
            answer.append(list(i)[0])
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{20,111},{111}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))