def solution(wallet, bill):
    # wallet: width x height
    # bill: width x height
    answer = 0
    
    while fit_in_wallet(wallet, bill):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        answer += 1
    return answer

def fit_in_wallet(wallet, bill):
    # Not rotated
    if (bill[0] <= wallet[0] and bill[1] <= wallet[1]):
        return False
    # Rotated
    if (bill[0] <= wallet[1] and bill[1] <= wallet[0]):
        return False
    return True


if __name__ == "__main__":
    wallet1 = [30, 15]
    bill1 = [26, 17]
    result1 = solution(wallet1, bill1)
    print(f"Test case 1: {result1}")  # Expected: 1

    wallet2 = [50, 50]
    bill2 = [100, 241]
    result2 = solution(wallet2, bill2)
    print(f"Test case 2: {result2}")  # Expected: 4
