n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

w_cnt = 0
b_cnt = 0
def check(matrix):
    white, blue = 0, 0
    global w_cnt, b_cnt
    n = len(matrix)
    for i in range(n):
        white += matrix[i].count(0)
        blue += matrix[i].count(1)
    if white == n*n:
        w_cnt += 1
        return True
    if blue == n*n:
        b_cnt += 1
        return True
    return False


def split(matrix):
    if check(matrix):
        return
    mid = len(matrix)//2
    new_matrix1 = [row[:mid] for row in matrix[:mid]]
    new_matrix2 = [row[mid:] for row in matrix[:mid]]
    new_matrix3 = [row[:mid] for row in matrix[mid:]]
    new_matrix4 = [row[mid:] for row in matrix[mid:]]

    split(new_matrix1)
    split(new_matrix2)
    split(new_matrix3)
    split(new_matrix4)

split(paper)
print(w_cnt)
print(b_cnt)