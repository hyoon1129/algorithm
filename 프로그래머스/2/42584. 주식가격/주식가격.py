def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
                idx = stack.pop()
                answer[idx] = i - idx
        else:
            stack.append(i)
    
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1
        
    return answer
