t = int(input())

tc = []
for i in range(t):
    tc.append(int(input()))
dp = [[] for _ in range(max(tc)+2)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, max(tc)+1):
    dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-1][0]]

for case in tc:
    print(dp[case][0], dp[case][1])