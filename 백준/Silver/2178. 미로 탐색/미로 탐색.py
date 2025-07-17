from collections import deque
n, m = map(int, input().split())

matrix = [[] for _ in range(n)]

for i in range(n):
    s = input()
    for num in s:
        matrix[i].append(int(num))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque([(0, 0, 1)])
    visited = [[False]*m for _ in range(n)]

    visited[0][0] = True

    while queue:
        x, y, cnt = queue.popleft()

        if x == m-1 and y == n-1:
            return cnt
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and matrix[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((nx, ny, cnt+1))

    return 0

print(bfs())