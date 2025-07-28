n = int(input())
home = []

for _ in range(n):
    home.append(list(map(int, input().split())))

# dp[i][j][k] = (i, j) 위치에 k 방향으로 끝점이 놓인 경우의 수
# k = 0: 가로, 1: 세로, 2: 대각선
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

# 초기값: (0, 1)에 가로 방향으로 파이프 시작
dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if home[i][j] == 1:
            continue

        # 1. 가로 방향(0)에서 오는 경우들
        if dp[i][j][0] > 0:
            # 가로 -> 가로
            if j + 1 < n and home[i][j+1] == 0:
                dp[i][j+1][0] += dp[i][j][0]

            # 가로 -> 대각선
            if (i+1 < n and j+1 < n and
                home[i][j+1] == 0 and home[i+1][j] == 0 and home[i+1][j+1] == 0):
                dp[i+1][j+1][2] += dp[i][j][0]

        # 2. 세로 방향(1)에서 오는 경우들
        if dp[i][j][1] > 0:
            # 세로 -> 세로 (아래로 이동)
            if i + 1 < n and home[i+1][j] == 0:
                dp[i+1][j][1] += dp[i][j][1]

            # 세로 -> 대각선 (대각선으로 이동)
            if (i + 1 < n and j + 1 < n and
                home[i][j+1] == 0 and home[i+1][j] == 0 and home[i+1][j+1] == 0):
                dp[i+1][j+1][2] += dp[i][j][1]

        # 3. 대각선 방향(2)에서 오는 경우들
        if dp[i][j][2] > 0:
            # 대각선 → 가로 (오른쪽으로 이동)
            if j + 1 < n and home[i][j + 1] == 0:
                dp[i][j + 1][0] += dp[i][j][2]

            # 대각선 → 세로 (아래로 이동)
            if i + 1 < n and home[i + 1][j] == 0:
                dp[i + 1][j][1] += dp[i][j][2]

            # 대각선 → 대각선 (대각선으로 이동)
            if (i + 1 < n and j + 1 < n and
                    home[i][j + 1] == 0 and home[i + 1][j] == 0 and home[i + 1][j + 1] == 0):
                dp[i + 1][j + 1][2] += dp[i][j][2]

result = dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2]
print(result)