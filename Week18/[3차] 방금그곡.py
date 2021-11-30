# 프로그래머스: 2018 KAKAO BLIND RECRUITMENT [3차] 방금그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683
def solution(m, musicinfos):
    answer = ''
    length = 0
    switch = {'C#': 'H', 'D#': 'I', 'F#': 'J', 'G#': 'K', 'A#': 'L'}
    if 'E#' in m:
        return "(None)"
    tmp = list(m)
    modify_m = []
    while tmp:
        now = tmp.pop(0)
        if tmp:
            if tmp[0] == '#':
                now += tmp.pop(0)
        if len(now) == 2:
            modify_m.append(switch[now])
        else:
            modify_m.append(now)
    m = ''.join(modify_m)
    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(',')
        minute = int(musicinfos[i][1][3:]) - int(musicinfos[i][0][3:])
        minute += 60*(int(musicinfos[i][1][:2]) - int(musicinfos[i][0][:2]))
        tmp = list(musicinfos[i][3])
        pitch = []
        while tmp:
            p = tmp.pop(0)
            if tmp:
                if tmp[0] == '#':
                    p += tmp.pop(0)
            if len(p) == 2:
                pitch.append(switch[p])
            else:
                pitch.append(p)
        if minute < len(musicinfos[i][3]):
            musicinfos[i][3] = ''.join(pitch[:minute])
        else:
            times = minute // len(musicinfos[i][3])
            mod = minute % len(musicinfos[i][3])
            musicinfos[i][3] = ''.join(pitch)*times
            musicinfos[i][3] += ''.join(pitch[:mod])
    for musicinfo in musicinfos:
        if m in musicinfo[3]:
            answer = musicinfo[2]
            # length = len(musicinfo[3])
    if answer == '':
        answer = "(None)"
    return answer


if __name__ == '__main__':
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
