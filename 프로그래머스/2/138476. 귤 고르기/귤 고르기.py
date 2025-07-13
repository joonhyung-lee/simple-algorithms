from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    counts = sorted(counter.values(), reverse=True)
    # print(counter)
    # print(counts)
    
    answer = 0
    total = 0
    for count in counts:
        total += count
        answer += 1
        if total >= k:
            break

    return answer