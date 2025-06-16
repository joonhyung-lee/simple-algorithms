def solution(n, computers):
    visited = [False] * n
    
    def dfs(idx):
        visited[idx] = True
        for _idx in range(n):
            if computers[idx][_idx] == 1 and not visited[_idx]:
                dfs(_idx)
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer