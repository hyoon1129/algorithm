n = int(input())

li = list(map(int, input().split()))

left = 0
right = n-1
temp = 10**11

ans_left = 0
ans_right = 0

while left < right:
    mid = li[left] + li[right]

    if abs(mid) < abs(temp):
        temp = abs(mid)
        ans_left = left
        ans_right = right

    if mid < 0:
        left += 1
    elif mid > 0:
        right -=1
    else:
        break


print(*sorted([li[ans_left], li[ans_right]]))