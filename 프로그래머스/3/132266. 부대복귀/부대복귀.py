from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = dict()
    
    for a, b in roads:
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
            
            
    visited = [False for i in range(n+1)]
    distance = [-1 for i in range(n+1)]
    
    queue = deque()
    queue.append((destination, 0))
    
    while queue:
        node, cnt = queue.popleft()
        
        if visited[node]:
            continue
        
        visited[node] = True
        distance[node] = cnt
        
        for i in graph[node]:
            queue.append((i, cnt+1))
            
    
    for i in sources:
        answer.append(distance[i])
    
    
    return answer