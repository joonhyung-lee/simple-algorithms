def solution(n):
    
    answer = 0
    for i in range(1, n+1):
        if n%i == 0:
            answer += i
    
    return answer

def test_solution():
    # Test 1
    assert solution(12) == 28, "Test case 1 failed"
    print("Test case 1: Passed")
    
    # Test 2
    assert solution(5) == 6, "Test case 2 failed"
    print("Test case 2: Passed")
    
if __name__ == "__main__":
    test_solution() 