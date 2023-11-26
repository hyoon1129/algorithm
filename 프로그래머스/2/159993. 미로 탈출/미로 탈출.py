from collections import deque


def bfs(start, end, maps):
    queue = deque()
    queue.append((start[0], start[1], 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[0] * len(maps[0]) for i in range(len(maps))]
    visited[start[0]][start[1]] = 1
    
    
    while queue:
        x, y, cnt = queue.popleft()
        if end == [x,y]:
            return cnt
        
        for i in range(4):
            ax, ay = x+dx[i], y+dy[i]
            if 0 <= ax < len(maps) and 0<= ay < len(maps[0]) and maps[ax][ay] != 'X':
                if visited[ax][ay] == 0:
                    visited[ax][ay] = 1
                    queue.append([ax, ay, cnt+1])
    return 0
    

def solution(maps):
    answer = 0
    global s, l, e
    s = []
    l = []
    e = []

    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s = [i,j]
            elif maps[i][j] == 'L':
                l = [i,j]
            elif maps[i][j] == 'E':
                e = [i,j]
                
    st = bfs(s,l, maps)
    le = bfs(l,e, maps)
    
    if st != 0 and le != 0:
        answer = st + le
    else:
        answer = -1
        
    return answer


