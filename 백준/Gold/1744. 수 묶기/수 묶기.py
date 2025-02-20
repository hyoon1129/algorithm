n = int(input())
negative = []
positive = []
zero = False
for i in range(n):
    num  = int(input())
    if num > 0:
        positive.append(num)
    elif num == 0:
        zero = True
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()
# 0은 무시.
# 음수는 음수 끼리 곱하기.
# li length 가 1이면 그대로 출력
# 1 1 이면 2

answer = 0

for i in range(0, len(negative) - 1, 2):
    answer += negative[i] * negative[i + 1]

if len(negative)%2 == 1:
    if not zero:
        answer += negative[-1]

for i in range(0, len(positive)-1, 2):
    if positive[i] + positive[i+1]  < positive[i] * positive[i+1]:
        answer += positive[i] * positive[i+1]
    else:
        answer += positive[i] + positive[i+1]
if len(positive) % 2 == 1:
    answer += positive[-1]

print(answer)