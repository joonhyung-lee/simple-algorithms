from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))
    count = 0
    
    while queue:
        index, sum = queue.popleft()
        if index == len(numbers):
            if sum == target:
                count += 1
            continue
        
        queue.append((index+1, sum+numbers[index]))
        queue.append((index+1, sum-numbers[index]))
        
    return count

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))