import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
respond_li = []
cnt = 0
for i in range(n):
    respond_li.append(list(map(str, input().split())))


def get_strike(test, number):
    test = list(map(int, str(test)))
    number = list(map(int, str(number)))

    strike = 0
    for i in range(3):
        if test[i] == number[i]:
            strike += 1
    return str(strike)

def get_ball(test, number):
    test = list(map(int, str(test)))
    number = list(map(int, str(number)))

    ball = 0
    for i in range(3):
        if number[i] in test and number[i]!=test[i]:
            ball += 1
    return str(ball)

num = ["1","2","3","4","5","6","7","8","9"]

for i in permutations(num,3):
    test = ''.join(list(i))
    k = 0
    while k < len(respond_li):
        testcase = respond_li[k]
        if [get_strike(test, testcase[0]), get_ball(test, testcase[0])] != testcase[1:]:
            break
        k += 1

    if k == len(respond_li):
        cnt += 1
print(cnt)