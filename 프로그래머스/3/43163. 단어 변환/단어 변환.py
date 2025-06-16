from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)
    queue = deque()
    queue.append((begin, 0))

    while queue:
        current, count = queue.popleft()
        if current == target:
            return count

        for i, word in enumerate(words):
            if not visited[i]:
                # 한 글자만 다르면 변환 가능
                diff = sum([1 for a, b in zip(current, word) if a != b])
                if diff == 1:
                    visited[i] = True
                    queue.append((word, count + 1))
    return 0