import sys
input = sys.stdin.readline
t, n = map(int, input().split())
player_loc = {}
player_item = {}
cheating = []
ban = []
for i in range(1, n+1):
    player_loc[str(i)] = '1'
    player_item[str(i)] = []
for _ in range(t):
    tmp = list(map(str, input().split()))
    num, player, code, factor = tmp[0], tmp[1], tmp[2], tmp[3:]
    if code == 'M':
        player_loc[player] = factor[0]
        # if factor[0] == player_loc[player]:
        #     cheating.append(num)
    elif code == 'F':
        if factor[0] != player_loc[player]:
            cheating.append(num)
        player_item[player].append(factor[0])
    elif code == 'C':
        a, b = factor[0] in player_item[player], factor[1] in player_item[player]
        if not (a and b):
            cheating.append(num)
        if a:
            player_item[player].remove(factor[0])
        if b:
            player_item[player].remove(factor[1])
    elif code == 'A':
        if player_loc[player] != player_loc[factor[0]]:
            cheating.append(num)
            ban.append(int(player))
ban = list(set(ban))
ban.sort()
print(len(cheating))
if len(cheating) != 0:
    print(' '.join(cheating))
print(len(ban))
if len(ban) != 0:
    print(' '.join(str(i) for i in ban))


