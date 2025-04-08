n, m = map(int, input().split())

board = []
b_first = ['W', 'B', 'W', 'B','W', 'B','W', 'B']
w_first = ['B', 'W', 'B', 'W','B', 'W','B', 'W']

b_board = []
w_board = []
for i in range(8):
    if i % 2 == 0:
        b_board.append(b_first)
        w_board.append(w_first)
    else:
        b_board.append(w_first)
        w_board.append(b_first)

for i in range(n):
    board.append(list(input()))

def solution(sw):
    b_cnt, w_cnt = 0, 0
    for i in range(8):
        for j in range(8):
            if sw[i][j] != b_board[i][j]:
                b_cnt += 1
            if sw[i][j] != w_board[i][j]:
                w_cnt += 1
    return min(b_cnt, w_cnt)

answer = []
for i in range(n-7):
    for j in range(m-7):
        sw = [rows[j:j+8] for rows in board[i:i+8]]
        answer.append(solution(sw))
print(min(answer))