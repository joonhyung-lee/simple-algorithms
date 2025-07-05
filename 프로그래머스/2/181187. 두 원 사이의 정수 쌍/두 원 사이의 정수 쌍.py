import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        max_y = math.floor((r2*r2 - x*x) ** 0.5)
        if r1*r1 - x*x > 0:
            min_y = math.ceil((r1*r1 - x*x) ** 0.5)
        else:
            min_y = 0
        answer += max(0, max_y - min_y + 1)
    return answer * 4