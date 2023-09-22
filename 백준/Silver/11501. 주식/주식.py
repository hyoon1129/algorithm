import sys
input = sys.stdin.readline

t = int(input())
li = []
for i in range(t):
    answer = 0
    n = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    now_max = 0
    for j in range(len(stock)):
        if stock[j] > now_max:
            now_max = stock[j]
        else:
            answer += now_max - stock[j]
    li.append(answer)
print(*li, sep = "\n")

'''
처음 제출한 코드는 입력이
1
4
6 4 7 2 일 때
넘어감 -> 구매 -> 판매 -> 넘어감
이어서 6을 구매하지 않아 3이 출력된다. 
첫날과 둘째날 6, 4를 구매하고 3일차에 팔아서 최대 이익 4를 만들어야 한다.

stock을 뒤에서부터 max를 찾아 그 전날 주가보다 max가 크면 
answer += max - 전 날 주가
를 하고
그 전날 주가가 max보다 크면
max를 그 전날 주가로 업데이트 한다.
'''
