import sys
input = sys.stdin.readline

n = int(input())
negative = [] # 음수 저장
positive = [] # 양수 저장
zero = False # 0이 있으면 false, 없으면 true

for i in range(n):
    a = int(input())
    if a > 0:
        positive.append(a)
    elif a == 0:
        zero = True
    else:
        negative.append(a)

positive.sort(reverse = True)
negative.sort()
answer = 0

if len(negative)%2 == 1: # 음수 개수가 홀수개면
    for i in range(0, len(negative)-1, 2):\
        answer += negative[i]*negative[i+1]
    if not zero: # 0이 dqjtdmaus
        answer += negative[-1]

else: # 음수 개수가 짝수개면
    for i in range(0, len(negative)-1, 2):
        answer += negative[i]*negative[i+1]


for i in range(0, len(positive) - 1, 2):
    if positive[i] + positive[i+1] < positive[i] * positive[i + 1]:
        answer += positive[i] * positive[i + 1]
    else:
        answer +=  positive[i] + positive[i+1]

if len(positive)%2 == 1:
    answer += positive[-1]


print(answer)