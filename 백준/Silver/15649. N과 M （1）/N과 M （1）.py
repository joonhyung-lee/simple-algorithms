def solve(N, M):
    used = [False] * (N + 1)
    sequence = []
    
    def backtrack():
        if len(sequence) == M:
            print(' '.join(map(str, sequence)))
            return
            
        for i in range(1, N + 1):
            if not used[i]:
                used[i] = True
                sequence.append(i)
                backtrack()
                sequence.pop()
                used[i] = False
    
    backtrack()

N, M = map(int, input().split())
solve(N, M)