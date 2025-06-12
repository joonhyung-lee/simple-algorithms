# 너비 우선 탐색 (Breadth-First Search, BFS)

너비 우선 탐색(BFS)은 그래프나 트리 구조에서 노드를 탐색하는 알고리이다. 시작 노드로부터 가까운 노드를 먼저 방문하고, 멀리 떨어진 노드를 나중에 방문하는 방식으로 동작한다.

## 특징

- 큐(Queue) 자료구조 사용
- 최단 경로 찾기에 유용
- 레벨 단위로 탐색 진행
- 시간 복잡도: O(V + E) (V: 정점 수, E: 간선 수) / 공간 복잡도: O(V)

## Python 구현 예제

### 1. 그래프에서의 BFS

```python
from collections import deque

def bfs(graph, start):
    visited = set()  # 방문한 노드를 저장하는 집합
    queue = deque([start])  # 탐색할 노드를 저장하는 큐
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()  # 큐에서 노드를 꺼냄
        print(vertex, end=' ')  # 현재 노드 출력
        
        # 현재 노드의 이웃 노드들을 확인
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 사용 예시
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS 탐색 결과:")
bfs(graph, 'A')  # 출력: A B C D E F
```

### 2. 2차원 그리드에서의 BFS (미로 탐색)

```python
from collections import deque

def maze_bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = set([(start[0], start[1])])
    
    # 상하좌우 이동
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        row, col, dist = queue.popleft()
        
        if (row, col) == end:
            return dist  # 도착점에 도달
        
        # 네 방향으로 이동 시도
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # 유효한 위치인지 확인
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                maze[new_row][new_col] == 0 and  # 0은 이동 가능한 칸
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
    
    return -1  # 도착점에 도달할 수 없는 경우

# 사용 예시
maze = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]

start = (0, 0)
end = (3, 3)
shortest_path = maze_bfs(maze, start, end)
print(f"\n시작점 {start}에서 도착점 {end}까지의 최단 거리: {shortest_path}")
```

## BFS의 활용

1. 최단 경로 찾기
2. 네트워크 탐색
3. 웹 크롤링
4. 소셜 네트워크에서의 관계 분석
5. 퍼즐 게임 솔버

## 시간 복잡도 분석

- 인접 리스트를 사용할 경우: O(V + E)
- 인접 행렬을 사용할 경우: O(V²)
- 추가 공간 복잡도: O(V)

여기서 V는 정점(Vertex)의 수, E는 간선(Edge)의 수를 의미한다.

## 장단점

### 장점
- 최단 경로를 보장
- 레벨 단위의 탐색이 필요한 경우 유용
- 두 노드 사이의 최단 경로 찾기에 적합

### 단점
- 메모리 사용량이 많음
- 모든 간선의 가중치가 동일한 경우에만 최단 경로 보장
- 깊이 우선 탐색(DFS)에 비해 구현이 약간 복잡
