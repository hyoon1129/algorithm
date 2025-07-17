import sys
input=sys.stdin.readline
n = int(input())

li = []

for _ in range(n):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    li.append([x, y])

li = sorted(li, key=lambda x:x[0])

answer = 0
now = li[0][0]
for x, y in li:
    if now > y:
        continue
    if now <= x:
        answer += (y-x)
    else:
        answer += (y-now)
    now = max(now, y)
print(answer)