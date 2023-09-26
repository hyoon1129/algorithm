import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
oper_num = list(map(int, input().split()))
oper_li = ["+","-","x","÷"]
operator = []
for i in range(4):
    if oper_num[i] != 0:
        for j in range(oper_num[i]):
            operator.append(oper_li[i])

def calculation(a, b, operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "x":
        return a*b
    else:
        if a > 0:
            return a//b
        else:
            return -(abs(a)//b)

max = - 10**9
min = 10**9

for oper_order in set(permutations(operator)):
    result = num[0]
    for i in range(n-1):
        a = result
        b = num[i+1]
        result = calculation(a, b, oper_order[i])
    if result > max:
        max = result
    if result < min :
        min = result
print(max, min)

# 같은 연산자 순서 바뀌는 경우도 모두 포함돼서 시간초과 났다. 순열에 set 넣어주니 풀리긴 풀렸다
# 근데 찾아보니 재귀로 풀면 겁나 빠름
