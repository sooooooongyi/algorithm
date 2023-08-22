# LV1 달리기경주
# 리스트.index() 보단 딕셔너리가 훨씬 빠름!
def solution(players, callings):
    answer = []
    rank = {player: i for i, player in enumerate(players)}
    for calling in callings:
        idx = rank[calling]
        rank[calling] -= 1
        rank[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players