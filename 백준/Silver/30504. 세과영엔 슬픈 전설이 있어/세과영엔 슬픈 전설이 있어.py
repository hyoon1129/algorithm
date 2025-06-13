n = int(input())
a = list(map(int, input().split()))  # i번째 날에 받아야 하는 최소 금액
b = list(map(int, input().split()))  # j번째 자루에 담은 금액

if sum(a) > sum(b):
    print(-1)
    exit()

b.sort()
amounts = []
answer = [0] * n

for i in range(n):
    amounts.append((a[i], i))
amounts.sort(key=lambda x: x[0])

for i in range(n):
    if amounts[i][0] > b[i]:
        print(-1)
        exit()
    answer[amounts[i][1]] = b[i]
print(*answer)