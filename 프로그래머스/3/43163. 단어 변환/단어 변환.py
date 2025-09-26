from collections import deque

def solution(begin, target, words):
    answer = 0
    
    queue = deque([(begin, 0)])
    
    visited = {}
    for word in words:
        visited[word] = False
    
    while queue:
        now, cnt= queue.popleft()
        if now == target:
            return cnt
        
        for word in words:
            if check(now, word) and not visited[word]:
                queue.append((word, cnt+1))
                visited[word] = True
    
    return 0

def check(a, b):
    cnt = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
            if cnt > 1:
                return False
    
    return True