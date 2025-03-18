n, m = map(int, input().split())

li = list(map(int, input().split()))

tc = []
for i in range(m):
    tc.append(list(map(int, input().split())))

dp = [0 for i in range(n+1)]
dp[1] = li[0]

for i in range(2,n+1):
    dp[i] = dp[i-1] + li[i-1]

for i, j in tc:
    print(dp[j]-dp[i-1])
