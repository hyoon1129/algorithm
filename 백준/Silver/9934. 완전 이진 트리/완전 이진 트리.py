import sys
input = sys.stdin.readline


k = int(input())
li = list(map(int, input().split()))

answer = [[] for i in range(k)]

for i in range(k):
    idx = max(0, 2**i-1)
    while idx < len(li):
        answer[i].append(li[idx])
        iter = 2**(i+1)
        idx += iter

for i in range(k-1, -1, -1):
    print(*answer[i])
