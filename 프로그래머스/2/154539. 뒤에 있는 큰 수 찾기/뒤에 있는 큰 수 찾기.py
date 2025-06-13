## 이전 코드
# def solution(numbers):
#     answer = []
#     bigger_number = 0
    
#     # O(n^2)
#     for idx, number in enumerate(numbers):
#         remainers = numbers[idx+1:]
#         # Set as default -1
#         bigger_number = -1

#         for remainer in remainers:
#             if number < remainer:  # 뒷 큰수를 찾으면
#                 bigger_number = remainer
#                 break  # 가장 가까운 큰 수를 찾았으므로 즉시 종료
        
#         answer.append(bigger_number)
#     return answer

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    # O(n)
    for i in range(len(numbers)):
        while stack and numbers[i] > stack[-1][1]:
            idx, _ = stack.pop()
            answer[idx] = numbers[i]
        stack.append((i, numbers[i]))
    return answer