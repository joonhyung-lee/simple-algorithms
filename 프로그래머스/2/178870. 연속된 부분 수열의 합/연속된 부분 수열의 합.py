def solution(sequence, k):
    n = len(sequence)
    left = 0
    right = 0
    curr_sum = sequence[0]
    answer = [0, n-1]

    while left < n and right < n:
        if curr_sum == k:
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
            left += 1
            if left <= right:
                curr_sum -= sequence[left-1]
            else:
                right = left
                if right < n:
                    curr_sum = sequence[right]
        elif curr_sum < k:
            right += 1
            if right < n:
                curr_sum += sequence[right]
        else:  # curr_sum > k
            curr_sum -= sequence[left]
            left += 1
            if left > right and left < n:
                right = left
                curr_sum = sequence[right]
    return answer