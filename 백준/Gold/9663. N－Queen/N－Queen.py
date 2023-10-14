import sys
input = sys.stdin.readline

n = int(input())
row = [0 for i in range(n)]
answer = 0

def n_queen(cnt):
    global answer
    if cnt == n:
        answer += 1
        return
    else:
        for i in range(n):
            row[cnt] = i
            for j in range(cnt):
                if row[cnt] == row[j] or abs((cnt-j)/(row[cnt]-row[j]))==1:
                    break
            else:
                n_queen(cnt+1)

n_queen(0)
print(answer)