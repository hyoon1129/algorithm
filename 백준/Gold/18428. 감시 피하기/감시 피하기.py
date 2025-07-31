import copy
from itertools import combinations

n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(str, input().split())))


candidate = []
teachers = []
students = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == "X":
            candidate.append([i, j])
        elif matrix[i][j] == "T":
            teachers.append([i, j])
        else:
            students.append([i, j])

def watch(x, y, temp_matrix):
    for i in range(x-1, -1, -1):
        if temp_matrix[i][y] == "S":
            return False
        elif temp_matrix[i][y] == "O":
            break

    for i in range(x+1, n):
        if temp_matrix[i][y] == "S":
            return False
        elif temp_matrix[i][y] == "O":
            break

    for i in range(y-1, -1, -1):
        if temp_matrix[x][i] == "S":
            return False
        elif temp_matrix[x][i] == "O":
            break

    for i in range(y+1, n):
        if temp_matrix[x][i] == "S":
            return False
        elif temp_matrix[x][i] == "O":
            break
    return True


def is_safe(temp_matrix):
    for tx, ty in teachers:
        if not watch(tx, ty, temp_matrix):
            return False
    return True

for combi in combinations(candidate, 3):
    temp_matrix = copy.deepcopy(matrix)
    for dx, dy in combi:
        temp_matrix[dx][dy] = "O"
    if is_safe(temp_matrix):
        print("YES")
        exit()
print("NO")