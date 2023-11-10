import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [[0,0]]
dp = [[0] * (k+1) for i in range(n+1)]

for i in range(n):
    bag.append(list(map(int, input().split())))


for y in range(1, n+1):
    w, v = bag[y]
    for x in range(1, k+1):
        if x < w : # 넣을 물건의 무게가 현재 허용 무게보다 크면
            dp[y][x] = dp[y-1][x] # 물건을 넣지 않음
        else:
            dp[y][x] = max(dp[y-1][x], dp[y-1][x-w]+v)

print(dp[n][k])


# dp[n][k]는 n번째 무게까지 살폈을 때, 무게가 k인 배낭의 최대 가치

# 물건을 배낭에 담을 때
# 1. 넣을 물건의 무게가 현재 배낭의 허용 무게보다 크면 넣지 않는다. (line 16~17)
# 2. 그렇지 않다면, 아래 두가지 경우 중 더 나은 가치를 선택한다. (line 19)
#   (1) 현재 배낭에서 넣을 물건의 무게만큼을 뺀 후, 현재 물건을 넣는다 (dp[y-1][x-w]+v)
#   (2) 현재 물건을 넣지 않고 그대로 가져간다. (dp[y-1][x])

# 2.(1) 에서, 배낭에서 넣을 물건의 무게만큼을 어케 빼나?? 그 물건의 무게와 같은 물건이 현재 배낭에 없으면?
# -> 상관 없다. 넣을 물건의 무게만큼을 뺀 배낭에는 그 무게의 배낭이 가질 수 있는 최대 가치가 저장되어 있다.

# 참고 : https://hongcoding.tistory.com/50