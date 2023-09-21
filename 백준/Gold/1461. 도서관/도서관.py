import sys
input = sys.stdin.readline

answer = 0


def getwalk(li):
    global answer
    if len(li) == 1:
        answer += li[0] * 2
        return


    while len(li)>0:
        answer += li[-1]*2
        li = li[:-m]


n, m = map(int, input().split())
li = list(map(int, input().split()))


li.sort()

left = []
right = []

for i in  li:
    if i < 0 :
        left.append(-i)
    else:
        right.append(i)

left.sort()
right.sort()

if left == []:
    left = [0]
if right == []:
    right = [0]

if left[-1] >= right[-1]:
    answer += left[-1]
    left = left[:-m]
else:
    answer += right[-1]
    right = right[:-m]
getwalk(left)
getwalk(right)
print(answer)

# m을 생각하지 못했다.. 그리고 left나 right가 []일때도........ 문제 잘 읽고 경우의 수 생각하기