# 2019 카카오 개발자 겨울 인턴십 : 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    lst = []
    # '},' 단위로 문자열 split
    test = tuple(map(str, s.split('},')))

    for i in test:
        # 문자열에서 '{', '}' 지우기
        tmp = i.replace('{', '')
        tmp = tmp.replace('}', '')
        # 숫자 튜플들만 추가
        lst.append(set(map(int, tmp.split(','))))
    # 길이 순서대로 정렬
    lst.sort()

    for i in lst:
        # 길이가 1일 경우 첫 숫자만 추가
        if len(i) == 1:
            answer.append(list(i)[0])
        # 길이가 2 이상의 튜플들에서 answer 리스트에 들어있지 않은 숫자들만 추가
        for j in i:
            if j not in answer:
                answer.append(j)
    # 결과값 반환
    return answer


# test code
# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{20,111},{111}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))