import math

def solution(storey):
    answer = 0
        
    while storey > 0:
        div = storey % 10
        if div > 5:
            answer += 10 - div
            storey += 10 - div
            
        elif div < 5:
            answer += div
            storey -= div
            
        else:
            if (storey // 10) % 10 >= 5:
                answer += 10 - div
                storey += 10 - div
            else:
                answer += div
                storey -= div

        storey //= 10
    return answer