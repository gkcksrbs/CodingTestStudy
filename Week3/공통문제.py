# 2021 카카오 채용연계형 인턴십 : 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

# key = 문자열, value: 숫자
str_to_num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
              'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def solution(s):
    for i in str_to_num:
        # 영어를 숫자로 바꾸기
        s = s.replace(i, str_to_num[i])
    # 정수형으로 결과값 반환
    return int(s)


# test code
print(solution("123"))
