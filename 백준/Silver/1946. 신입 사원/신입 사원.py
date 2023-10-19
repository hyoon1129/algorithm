import sys
input = sys.stdin.readline

t = int(input())

def solution(n, rank):
    fail = 0
    rank.sort()
    num = rank[0][1]
    for i in range(1, n):
        if rank[i][1] > num:
            fail += 1
        else:
            num = rank[i][1]
    return n-fail


answer = []
for i in range(t):
    n = int(input())
    rank = []

    for j in range(n):
        rank.append(list(map(int, input().split())))
    answer.append((solution(n, rank)))
for a in answer:
    print(a)