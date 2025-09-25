from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(maps, n, m):
    global dx, dy
    queue = deque([(0, 0, 1)]) # x, y, cnt
    visited = [[False] * m for _ in range(n)]
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == m-1 and y == n-1:
            return cnt
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maps[ny][nx] != 0:
                queue.append((nx, ny, cnt+1))
                visited[ny][nx] = True

    return -1


def solution(maps):
    return bfs(maps, len(maps), len(maps[0]))