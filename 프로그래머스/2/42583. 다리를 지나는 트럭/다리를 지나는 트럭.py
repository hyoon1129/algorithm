from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0 for _ in range(bridge_length)])
    
    i = 0
    total = 0
    while i < len(truck_weights):
        if total - queue[0] + truck_weights[i] <= weight:
            queue.append(truck_weights[i])
            total += truck_weights[i]
            i += 1
        else:
            queue.append(0)
        total -= queue[0]
        queue.popleft()
        answer += 1
        
    answer += bridge_length
    
    return answer