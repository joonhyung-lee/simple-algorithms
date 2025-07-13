from collections import deque

def solution(x, y, n):
    visited = [False] * (y + 1)
    queue = deque()
    queue.append((x, 0))  # (current #, calculation #)
    visited[x] = True

    while queue:
        current, count = queue.popleft()
        if current == y:
            return count
        
        for next_num in (current + n, current * 2, current * 3):
            if next_num <= y and not visited[next_num]:
                visited[next_num] = True
                queue.append((next_num, count + 1))
    return -1