# 깊이 우선 탐색 (Depth-First Search, DFS)

깊이 우선 탐색(DFS)은 그래프나 트리 구조에서 가능한 한 깊이 내려가면서 노드를 탐색하고, 더 이상 방문할 수 없을 때 백트래킹하는 알고리즘이다.

## 특징

- 스택(Stack) 자료구조 사용 또는 재귀 함수로 구현
- 경로 탐색에 적합
- 백트래킹에 유용
- 시간 복잡도: O(V + E) (V: 정점 수, E: 간선 수) / 공간 복잡도: O(V)

## Python 구현 예제

### 1. 재귀를 사용한 DFS

```python
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(vertex)
    print(vertex, end=' ')
    
    # 현재 노드의 이웃 노드들을 재귀적으로 방문
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# 사용 예시
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS 재귀 탐색 결과:")
dfs_recursive(graph, 'A')  # 출력: A B D E F C
```

### 2. 스택을 사용한 DFS

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            
            # 현재 노드의 이웃 노드들을 스택에 추가
            # 역순으로 추가하여 원하는 순서로 방문
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

print("\nDFS 반복 탐색 결과:")
dfs_iterative(graph, 'A')  # 출력: A B D E F C
```

### 3. 미로 탐색 DFS

```python
def maze_dfs(maze, start, end, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    rows, cols = len(maze), len(maze[0])
    row, col = start
    
    # 현재 위치가 도착점인 경우
    if (row, col) == end:
        path.append((row, col))
        return path
    
    # 현재 위치를 방문 처리
    visited.add((row, col))
    path.append((row, col))
    
    # 상하좌우 이동
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        
        # 유효한 위치인지 확인
        if (0 <= new_row < rows and 
            0 <= new_col < cols and 
            maze[new_row][new_col] == 0 and 
            (new_row, new_col) not in visited):
            
            result = maze_dfs(maze, (new_row, new_col), end, path, visited)
            if result:
                return result
    
    # 현재 경로가 실패한 경우 백트래킹
    path.pop()
    return None

# 사용 예시
maze = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]

start = (0, 0)
end = (3, 3)
path = maze_dfs(maze, start, end)
print(f"\n미로 경로: {path}")
```

## DFS의 활용

1. 경로 찾기 문제
2. 위상 정렬
3. 사이클 탐지
4. 퍼즐 게임 솔버
5. 백트래킹 문제 해결

## DFS vs BFS

### DFS 장점
- 메모리 사용량이 적음 (한 경로당 노드만 저장)
- 목표 노드가 깊은 단계에 있을 때 유리
- 백트래킹에 적합

### DFS 단점
- 최단 경로를 보장하지 않음
- 무한 깊이 문제 발생 가능
- 목표 노드가 얕은 단계에 있을 때 비효율적

### 선택 기준
- DFS: 모든 노드를 방문해야 할 때, 백트래킹이 필요할 때
- BFS: 최단 경로를 찾아야 할 때, 레벨 단위 탐색이 필요할 때

## 시간 복잡도 분석

- 인접 리스트 사용: O(V + E)
- 인접 행렬 사용: O(V²)
- 공간 복잡도: O(V)

V는 정점(Vertex)의 수, E는 간선(Edge)의 수를 의미한다.
