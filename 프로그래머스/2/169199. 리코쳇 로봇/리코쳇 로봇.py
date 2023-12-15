from collections import deque

def bfs(start, target, board):
    queue = deque()
    queue.append((start[0], start[1]))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[0] * len(board[0]) for i in range(len(board))]
    visited[start[0]][start[1]] = 1
    
    while queue:
        x, y = queue.popleft()
        if [x, y] == target:
            return visited[x][y]
    
        for i in range(4):
            nx, ny = x, y
            while True:
                nx, ny = nx+dx[i], ny+dy[i]
                if (0<= nx < len(board)) and (0<= ny < len(board[0])) and (board[nx][ny] == "D"):
                    nx = nx - dx[i]
                    ny = ny - dy[i]
                    break
                    
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                    nx = nx - dx[i]
                    ny = ny - dy[i]
                    break
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1
        
        
        

def solution(board):
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                start = [i,j]
            elif board[i][j] == "G":
                target = [i,j]
                
    answer = bfs(start,target, board)
    if answer == -1:
        return answer
    else:
        return answer - 1