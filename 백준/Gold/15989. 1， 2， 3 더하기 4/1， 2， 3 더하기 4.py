t = int(input())

tc = [int(input()) for _ in range(t)]
n = max(tc)


dp = [0] * (n+1)
dp[0] = 1

for num in [1,2,3]:
    for i in range(num, n+1):
        dp[i] += dp[i-num]

for case in tc:
    print(dp[case])