from collections import deque

n, k = map(int, input().split())

money = deque()

for i in range(n):
    coin = int(input())
    if coin > k:
        break
    else:
        money.append(coin)

answer = 0
while k > 0:
    now = money.pop()
    if k >= now:
        answer += k//now
        k -= (k//now)*now

print(answer)