def solution(players, callings):
    player_rank = {player: i for i, player in enumerate(players)}
    
    for winner in callings:
        i = player_rank[winner]
        
        loser = players[i - 1] 
        
        players[i], players[i-1] = players[i-1], players[i]
        player_rank[winner], player_rank[loser] = i - 1, i
        
    return players