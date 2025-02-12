def solution(money):
    answer = 0
    dp1 = [0 for i in range(len(money))] # 첫 번째 집을 터는 경우
    dp2 = [0 for i in range(len(money))] # 첫 집 안털고 두 번째 집 터는 경우
    
    dp1[0] = money[0] 
    for i in range(1, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
    
    dp2[0] = 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
    
    
    
    return max(dp1[-2], dp2[-1])