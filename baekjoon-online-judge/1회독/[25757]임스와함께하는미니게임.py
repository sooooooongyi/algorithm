# 🌜, ✨ 몫, set 문제

n, game = map(str, input().split())
games = [('Y', 2), ('F', 3), ('O', 4)]
players = []

for _ in range(int(n)):
    player = input()
    players.append(player)
    
players = set(players)
pLen = len(players)

if game == 'Y':
    print(pLen)
    
if game == 'F':
    print(pLen // 2)
    
if game == 'O':
    print(pLen // 3)