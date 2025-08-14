from collections import deque
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

def bfs():
    visited = [[False]*m for _ in range(n)]
    dist = [[-1] * m for _ in range(n)]
    queue = deque([])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                queue.append((j, i))
                dist[i][j] = 0
    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and matrix[ny][nx] != 1:
                queue.append((nx, ny))
                dist[ny][nx] = dist[y][x] + 1
                visited[ny][nx] = True

    result = 0
    for i in range(n):
        result = max(result, max(dist[i]))
    return result

print(bfs())