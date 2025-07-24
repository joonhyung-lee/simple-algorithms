import math

def solution(progresses, speeds):
    answer = []
    # Get remain days
    day = [math.ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    
    # Get distribute days
    cnt = 1
    cumulative_day = day[0]
    for _d in day[1:]:
        if _d <= cumulative_day:
            cnt += 1
        else:
            answer.append(cnt)
            cumulative_day = _d
            cnt = 1
    answer.append(cnt)
    return answer