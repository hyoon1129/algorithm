a, b = map(int, input().split())
r = int(input())

visited = [[False] * r for _ in range(r)]
visited[a][b] = True

cnt = 0
x, y = a, b
while True:
    if (x+1) + (y+1) < r:
        x += 1
        y += 1
    else:
        x //= 2
        y //= 2
    cnt += 1
    if visited[x][y] == True:
        break
    visited[x][y] = True

print(cnt)