def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    count = 0
    
    for _idx, _s in enumerate(s):
        if _s == "(":
            count += 1
        elif _s == ")":
            count -= 1
        
        if count < 0:
            return False
    
    return count == 0