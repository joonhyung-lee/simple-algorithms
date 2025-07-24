def solution(clothes):
    answer = 1

    _dict = {}
    for v, k in clothes:
        if k not in _dict:
            _dict[k] = []
        _dict[k].append(v)
    
    # count for all of the clothes: (wear, unwear) then -1
    for k in _dict:
        answer *= (len(_dict[k]) + 1)

    return answer -1