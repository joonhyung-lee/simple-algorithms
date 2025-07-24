def solution(s):
    count = 0
    
    for _s in s:
        if _s == "(":
            count += 1
        elif _s == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0