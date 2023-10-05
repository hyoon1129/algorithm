import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
dx = [-2, -1, -2, -1, 1, 2, 1, 2]
dy = [-1, -2, 1, 2, -2, -1, 2, 1]

def bfs(x, y, visited, target):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        if target == [x,y]:
            return visited[x][y] - 1
        for i in range(8):
            if (0 <= x+dx[i] < l and 0<= y+dy[i] <l ):
                if visited[x+dx[i]][y+dy[i]] == 0:
                    queue.append((x+dx[i], y+dy[i]))
                    visited[x+dx[i]][y+dy[i]] = visited[x][y] + 1


result = []

for i in range(n):
    l = int(input())
    now = list(map(int, input().split()))
    target = list(map(int, input().split()))
    visited = [[0] * l for i in range(l)]
    result.append(bfs(now[0], now[1], visited, target))

for i in result:
    print(i)