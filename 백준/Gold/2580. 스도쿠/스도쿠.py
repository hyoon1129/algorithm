import sys
input = sys.stdin.readline

matrix = []
blank = [] # 비어 있는 좌표 저장
for i in range(9):
    matrix.append(list(map(int, input().split())))
    for j in range(9):
        if matrix[i][j] == 0:
            blank.append([i, j])




def line(pos, value):
    global matrix
    column = matrix[pos[0]]
    for i in range(9):
        if value == column[i]:
            return False

    row = [t[pos[1]] for t in matrix]

    for i in range(9):
        if value == row[i]:
            return False

    return True

def section(pos, value):
    arr = []
    for i in range((pos[0]//3)*3, (pos[0]//3)*3+3):
        for j in range((pos[1]//3)*3, (pos[1]//3)*3+3):
            arr.append(matrix[i][j])

    for i in range(9):
        if value == arr[i]:
            return False
    return True

def sudoku(n):
    global matrix
    if n == len(blank):
        for i in matrix:
            print(*i)
        exit(0)

    for i in range(1,10):
        x = blank[n][0]
        y = blank[n][1]
        if line(blank[n], i) and section(blank[n], i):
            matrix[x][y] = i
            sudoku(n+1)
            matrix[x][y]=0

sudoku(0)