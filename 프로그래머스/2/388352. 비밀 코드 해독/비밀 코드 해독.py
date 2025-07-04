from itertools import combinations

def solution(n, q, ans):
    answer = 0
    nums = list(range(1, n+1))
    
    # All of the combinations
    for _comb in combinations(nums, 5):
        _valid = True
        _comb_set = set(_comb)
        for _q, _a in zip(q, ans):
            if len(_comb_set & set(_q)) != _a:
                _valid = False
                break
        if _valid:
            answer += 1
    return answer