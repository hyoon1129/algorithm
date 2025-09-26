def solution(n, computers):
    answer = 0
    
    stack = []
    stack.append(1)
    
    visited = [False]*n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            stack = [i]
            visited[i] = True
            while stack:
                current = stack.pop()
                
                for j in range(n):
                    if computers[current][j] and not visited[j]:
                        stack.append(j)
                        visited[j] = True
    
    return answer