# 1. 주식을 하나 산다
# 2. 원하는 만큼 가지고 있는 주식을 판다
# 3. 아무 것도 안한다

# 날 별로 주식의 가격을 알려 줬을 때 최대 이익이 얼마나 되는지 계산
# 계속 감소하면 최대 이익 0

t = int(input())
answer = []

def getProfit(n, day):
    max_price = 0
    profit = 0
    for price in day[::-1]:
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price
    return profit

for i in range(t):
    n = int(input())
    day = list(map(int, input().split()))
    answer.append(getProfit(n, day))

for i in range(t):
    print(answer[i])