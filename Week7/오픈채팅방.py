# 코딩테스트 연습 2019 KAKAO BLIND RECRUITMENT 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(records):
    result = []
    data = dict()

    for record in records:
        tmp = record.split()

        if tmp[0] == 'Enter':
            data[tmp[1]] = tmp[-1]
            result.append(tmp[1] + "님이 들어왔습니다.")
        elif tmp[0] == 'Leave':
            result.append(tmp[1] + "님이 나갔습니다.")
        else:
            data[tmp[1]] = tmp[-1]

    for i in range(len(result)):
        uid = result[i].split()[0][:-2]
        result[i] = result[i].replace(uid, data[uid])

    return result


if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
                    "Change uid4567 Ryan"]))
