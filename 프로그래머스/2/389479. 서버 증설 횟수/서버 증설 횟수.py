def solution(players, m, k):
    history = []
    
    for player in players:
        # 가용되고 있는 서버 확인
        total = sum((history + [1])[-k:]) * m

        # player 수가 더 적다면
        if total > player:
            history = history + [0]
        # 서버 증설
        else:
            add = (player - total) // m + 1
            history += [add]

    return sum(history)