from collections import deque
t = int(input())


def test_case():
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    return m, n, matrix

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(m, n, matrix, visited, x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < m and 0<= ny < n:
                if matrix[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append([nx, ny])
    return


cnt = 0
for i in range(t):
    cnt = 0
    m, n, matrix = test_case()
    visited = [[False] * m for _ in range(n)]
    for j in range(n):
        for k in range(m):
            if matrix[j][k] == 1 and not visited[j][k]:
                bfs(m, n, matrix, visited, k, j)
                cnt += 1
    print(cnt)