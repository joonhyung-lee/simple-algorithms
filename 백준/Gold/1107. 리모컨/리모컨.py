def is_broken(number, broken_buttons):
    if number in broken_buttons:
        return True
    else:
        return False

def can_make_number(number, broken_buttons):
    if number == 0:
        if is_broken(0, broken_buttons):
            return 0
        else:
            return 1
    
    count = 0 
    temp = number
    
    while temp > 0:
        digit = temp % 10
        if is_broken(digit, broken_buttons):
            return 0
        count += 1
        temp //= 10
    return count

def solve(target, broken_buttons):
    if target == 100:
        return 0
        
    min_count = abs(target - 100)
    
    for channel in range(1000001):
        length = can_make_number(channel, broken_buttons)
        
        if length:
            press = length + abs(target - channel)
            min_count = min(min_count, press)
    
    return min_count

# 입력
N = int(input())
M = int(input())
broken = []
if M > 0:
    broken = list(map(int, input().split()))

print(solve(N, broken))