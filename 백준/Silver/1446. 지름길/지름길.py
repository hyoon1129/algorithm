n, d = map(int, input().split())

dic = {}
for i in range(n):
    s, e, r = map(int, input().split())
    if s in dic:
        dic[s].append([e, r])
    else:
        dic[s] = [[e, r]]

answer = 0
dp = [i for i in range(d+1)]

for i in range(d):
    if i in dic:
        for e, r in dic[i]:
            if e <= d:
                dp[e] = min(dp[e], dp[i]+r)
    dp[i+1] = min(dp[i]+1,dp[i+1])

print(dp[d])