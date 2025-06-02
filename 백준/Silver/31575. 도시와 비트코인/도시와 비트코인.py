from collections import deque

n, m = map(int, input().split())

matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split())))

dx = [1, 0]
dy = [0, 1]

def bfs():
    queue = deque()

    queue.append((0,0))
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True

    while queue:
        nx, ny = queue.popleft()
        if nx == m - 1 and ny == n - 1:
            return True


        for i in range(2):
            x, y = nx + dx[i], ny +dy[i]

            if 0 <= x < m and 0 <= y < n and matrix[x][y] == 1 and not visited[x][y]:
                queue.append((x, y))
                visited[x][y] = True
    return False

if bfs():
    print("Yes")
else:
    print("No")
