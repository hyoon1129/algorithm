from collections import deque
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

def bfs(a, b):
    visited = [[False]*m for _ in range(n)]
    queue = deque([(a, b, 0)])
    visited[b][a] = True
    dist = []

    while queue:
        x, y, cnt = queue.popleft()

        if matrix[y][x] == 1:
            dist.append(cnt)
            continue

        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                queue.append((nx, ny, cnt+1))
                visited[ny][nx] = True

    if dist:
        return min(dist)
    else:
        return 0

result = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] != 1:
            result.append(bfs(j, i))

print(max(result))