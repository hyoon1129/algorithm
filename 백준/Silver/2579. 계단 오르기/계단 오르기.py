import sys
input = sys.stdin.readline

n = int(input())
step = []
step.append(0)

for i in range(n):
    step.append(int(input()))

if n<3:
    print(sum(step))
else:

    dp = [0] * (n+1)
    dp[1] = step[1]
    dp[2] = dp[1] + step[2]
    dp[3] = max(dp[1]+step[3], step[2]+step[3])

    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+step[i-1]+step[i], dp[i-2]+step[i])

    print(dp[n])


# dp[n] = dp[n-2] + step[n] 전 계단 뛰어넘고 올 때
# OR
# dp[n] = dp[n-3] + step[n-1] + step[n] 전전계단 뛰어넘고 올 때