r, c, k = map(int, input().split())

matrix = [list(input().strip()) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = 0

visited = [[False]*c for _ in range(r)]

visited[r-1][0] = True
def dfs(y, x, dist):
    global answer
    if (y, x) == (0, c-1):
        if dist == k:
            answer += 1
            return
    if dist == k:
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx] and matrix[ny][nx] != "T":
            visited[ny][nx] = True
            dfs(ny, nx, dist+1)
            visited[ny][nx] = False
    return

dfs(r-1, 0, 1)
print(answer)