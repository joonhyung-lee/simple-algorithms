def solution(s):
    idx = 0
    answer = 1
    
    while idx < len(s):
        l, r = idx, idx
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            answer = max(answer, r-l+1)
            l -= 1
            r += 1
        
        l, r = idx, idx+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            answer = max(answer, r-l+1)
            l -= 1
            r += 1

        idx += 1
    return answer