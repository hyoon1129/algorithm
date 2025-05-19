n, k = map(int, input().split())

temp = list(map(int, input().split()))

dp = [0 for _ in range(n)]

dp[0] = temp[0]

for i in range(1, n):
    dp[i] = dp[i-1] + temp[i]

sum_li = [0 for _ in range(n-k+1)]
sum_li[0] = dp[k-1]

for i in range(1, n-k+1):
    sum_li[i] = dp[i+k-1] - dp[i-1]

print(max(sum_li))