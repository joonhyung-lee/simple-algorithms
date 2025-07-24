## Using Deque
# from collections import deque

# def solution(scoville, K):
#     answer = 0
#     s_queue = deque(scoville) # O(N)

#     while s_queue[0] < K: # O(1)
#         # mix
#         new_scoville = s_queue[0] + s_queue[1]*2    # O(1)
#         s_queue.popleft()   # O(1)
#         s_queue.popleft()   # O(1)
#         s_queue.appendleft(new_scoville)    # O(1)
#         # sort
#         s_queue = deque(sorted(s_queue))    # O(MlogM)
#         answer += 1
#         if len(s_queue) == 1:    # O(1)
#             return -1
#     return answer

## Using HeapQ
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+second*2)
        answer += 1

    return answer
