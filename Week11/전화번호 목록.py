# 프로그래머스 해시 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer


if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["12","123","1235","567","88"]))