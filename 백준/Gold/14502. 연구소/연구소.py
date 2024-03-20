import copy
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(matrix):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                queue.append((i,j))
                visited[i][j] = 1


    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0 and visited[nx][ny] == 0:
                    matrix[nx][ny] = 2
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

    answer.append(count_safe(matrix))
    return



arr = []

def wall(matrix, cnt, arr):
    if cnt == 3:
        arr.append(copy.deepcopy(matrix))
        return

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                wall(matrix, cnt + 1, arr)
                matrix[i][j] = 0




def count_safe(matrix):
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                count += 1

    return count

wall(matrix,0, arr)

answer = []
for combi in arr:
    temp = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(m):
            if combi[i][j] == 1:
                temp[i][j] = 1
    bfs(temp)

print(max(answer))