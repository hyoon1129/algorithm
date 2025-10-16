from collections import deque
h, w = map(int, input().split())
board = []
for _ in range(h):
    board.append(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = 0

def bfs(start_x, start_y):
    queue = deque()
    visited = [[-1]*w for _ in range(h)]
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 0
    max_dist = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == -1 and board[nx][ny] == 'L':
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                max_dist = max(max_dist, visited[nx][ny])
    return max_dist

for i in range(h):
    for j in range(w):
        if board[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)