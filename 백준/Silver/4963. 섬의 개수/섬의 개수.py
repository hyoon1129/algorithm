import sys
sys.setrecursionlimit(10 ** 6)

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]
visited = []
def dfs(x, y):
    visited[y][x] = True

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx  < w and 0 <= ny < h:
            if not visited[ny][nx] and matrix[ny][nx] == 1:
                dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0

    for y in range(h):
        for x in range(w):
            if matrix[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1

    print(count)