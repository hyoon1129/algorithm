n = int(input())

li = []
for i in range(n):
    a, b = map(int, input().split())
    li.append([a,b])

li.sort()

B = [b for a, b in li]

dp = [1] * n
for i in range(n):
    for j in range(i):
        if B[j] < B[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))