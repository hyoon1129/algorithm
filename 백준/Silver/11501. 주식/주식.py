import sys
input = sys.stdin.readline

t = int(input())
li = []
for i in range(t):
    answer = 0
    n = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    now_max = 0
    for j in range(len(stock)):
        if stock[j] > now_max:
            now_max = stock[j]
        else:
            answer += now_max - stock[j]
    li.append(answer)
print(*li, sep = "\n")