from collections import deque
n = int(input())

matrix = [[] for _ in range(n)]
for i in range(n):
    s = input()
    for num in s:
        matrix[i].append(int(num))


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0
def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    complex = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                complex += 1
                queue.append((nx, ny))
    return complex

visited = [[False]*n for _ in range(n)]
complexes = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            continue
        if matrix[i][j] == 1 and not visited[i][j]:
            complexes.append(bfs(i, j, visited))
            cnt += 1

print(cnt)
for num in sorted(complexes):
    print(num)