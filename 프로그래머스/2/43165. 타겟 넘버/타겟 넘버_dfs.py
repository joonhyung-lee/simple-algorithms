def solution(numbers, target):
    def dfs(index, sum):
        if index == len(numbers):
            if sum == target:
                return 1
            else:
                return 0
        return dfs(index+1, sum+numbers[index]) + dfs(index+1, sum-numbers[index])
    return dfs(0, 0)

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))