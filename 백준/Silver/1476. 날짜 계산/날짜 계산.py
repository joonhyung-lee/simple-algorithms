def solve(e, s, m):
    if not (1 <= e <= 15 and 1 <= s <= 28 and 1 <= m <= 19):
        return None
    
    # 나머지 연산
    e -= 1
    s -= 1
    m -= 1
    
    year = 1
    while year <= 7980:  # 15*28*19
        if (year-1) % 15 == e and (year-1) % 28 == s and (year-1) % 19 == m:
            return year
        year += 1
    
    return None

e, s, m = map(int, input().split())
result = solve(e, s, m)
if result:
    print(result)