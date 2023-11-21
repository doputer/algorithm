def solution(players, callings):
    rank = {player: r for r, player in enumerate(players)}

    for call in callings:
        curr_rank = rank[call]

        rank[call], rank[players[curr_rank - 1]] = rank[call] - \
            1, rank[players[curr_rank - 1]] + 1
        players[curr_rank], players[curr_rank -
                                    1] = players[curr_rank - 1], players[curr_rank]

    return players
