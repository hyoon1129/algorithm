n = int(input())
a = list(map(int, input().split()))

left = 0
right = n-1

answer = 10**9

while left < right:
    temp = a[left] + a[right]

    if temp < 0:
        left += 1
    elif temp == 0:
        answer = 0
        break
    else:
        right -=1

    if abs(answer) > abs(temp):
        answer = temp
print(answer)