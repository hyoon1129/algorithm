n = int(input())
li = list(map(int, input().split()))

total = sum(li)
answer = 0

li = sorted(li)

for i in range(n):
    length = li[i]

    total-= length
    answer += total * length

print(answer)