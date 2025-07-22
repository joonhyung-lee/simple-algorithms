def solution(people, limit):
    answer = 0

    people.sort()
    print(people)
    left = 0
    right = len(people) - 1
    
    while left <= right:
        sum = people[left] + people[right]
        if sum <= limit:
            left += 1
        right -= 1
        answer += 1
        
    return answer