n = int(input())

wine = []
for i in range(n):
    wine.append(int(input()))

dp = [0 for _ in range(n)]

# i번째 포도주를 안 마신다
# i번째 포도주를 먹고 i-1번째를 안 마신다
# i번째, i-1번째 포도주를 먹고 i-2번째는 안 마신다

if n == 1:
    print(wine[0])
    exit()
elif n == 2:
    print(wine[0] + wine[1])
    exit()
    
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0]+wine[2], wine[1]+wine[2], dp[1])
    
for i in range(3, n):
    dp[i] = max(
        dp[i-1],
        dp[i-2] + wine[i],
        dp[i-3] + wine[i-1] + wine[i]
    )
print(dp[n-1])