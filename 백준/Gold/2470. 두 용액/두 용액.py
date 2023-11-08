import sys
input = sys.stdin.readline

n = int(input())
li = sorted(list(map(int, input().split())))


# [-99, -2, -1, 4, 105]
# [1, 2, 3, 4, 5]
# [-2, 0, 1, 6]
start, end = 0, n - 1
minimun = li[start] + li[end]
answer = [li[start], li[end]]



while start < end :
    if abs(minimun) > abs(li[start] + li[end]) :
        minimun = li[start] + li[end]
        answer = [li[start], li[end]]
    elif li[start] + li[end] < 0:
        start = start + 1
    else:
        end = end - 1

for i in answer:
    print(i, end = " ")
