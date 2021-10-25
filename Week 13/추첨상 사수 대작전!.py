# 2020 아주대학교 프로그래밍 경시대회 APC - Div.1

# Easy
m, seed, x1, x2 = map(int, input().split())
found = False
a = 0
while a <= m and not found:
    for c in range(m+1):
        if (a*seed+c) % m == x1 and (a*x1+c) % m == x2:
            print(a, c)
            found = True
        if found:
            break
    a += 1
