def solution(m, n, puddles):
    m, n = n, m
    
    dp = [[0] * (n+1) for i in range(m+1)]
    puddle = [[0] * (n+1) for i in range(m+1)]
    
    # 웅덩이 위치를 1로 표기
    for x, y in puddles:
        puddle[y][x] = 1
        
    dp[1][1] = 1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if [i,j] == [1,1]:
                continue
            if puddle[i][j] == 1:
                continue
                
            # [i][j]까지 갈 수 있는 경우의 수는,
            # 바로 위까지 갈 수 있는 경우의 수 + 바로 왼쪽까지 갈 수 있는 경우의 수
            dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        
    return dp[m][n]%1000000007