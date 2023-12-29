from collections import deque

def bfs(x,y,n):
    queue = deque()
    dic = {}
    queue.append((x, 0))
    dic[x] = 0
    
    while queue:
        nx, cnt = queue.popleft()
        
        if nx == y:
            return cnt
        
        for i in range(3):
            ax = 연산(nx, n, i)
            if ax <= y and ax not in dic:
                queue.append((ax, cnt+1))
                dic[ax] = cnt+1
    return -1

def 연산(x, n, i):
    if i == 0:
        return x+n
    elif i == 1:
        return x*2
    else:
        return x*3
            
        
def solution(x, y, n):
    return bfs(x,y,n)