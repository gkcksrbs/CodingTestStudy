import sys
input = sys.stdin.readline
birth = input()
n = int(input())
bio = [0]*8
lst = {}
answer = int(1e9)
max_num = 0
for _ in range(n):
    date = input()
    for i in range(8):
        bio[i] = (int(birth[i]) - int(date[i]))**2
    year, month, day = sum(bio[:4]), sum(bio[4:6]), sum(bio[6:])
    if max_num <= year*month*day:
        if max_num == year*month*day and answer > int(date):
            answer = int(date)
        else:
            answer = int(date)
            max_num = year*month*day
print(answer)