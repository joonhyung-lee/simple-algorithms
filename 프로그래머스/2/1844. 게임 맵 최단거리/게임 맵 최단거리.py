from collections import deque

def solution(maps):
    # rows
    n = len(maps)
    # cols
    m = len(maps[0])
    # directions
    dx = [-1, 1, 0, 0]  
    dy = [0, 0, -1, 1]
    # distance
    distance = [[-1] * m for _ in range(n)]
    distance[0][0] = 1
    
    queue = deque([(0,0)])
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    return distance[n-1][m-1]