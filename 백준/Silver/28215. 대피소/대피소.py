from itertools import combinations

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

N, K = map(int, input().split())
H = [tuple(map(int, input().split())) for _ in range(N)]

answer = float('inf')
for shelters in combinations(H, K):
    max_distance = 0
    for home in H:
        min_distance = min(distance(home, shelter) for shelter in shelters)
        max_distance = max(max_distance, min_distance)
    answer = min(answer, max_distance)
print(answer)