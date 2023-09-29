import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
matrix = []
member = []

for i in range(n):
    li = list(map(int, input().split()))
    matrix.append(li)
    member.append(i+1)

def get_s(li):
    total = 0
    if len(li) == 2:
        return matrix[li[0]-1][li[1]-1] + matrix[li[1]-1][li[0]-1]
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            total +=  matrix[li[i]-1][li[j]-1] + matrix[li[j]-1][li[i]-1]

    return total

answer = 10**8

for i in range(2, n//2+1):
    difference = 0
    for k in combinations(member,i):
        start = list(k)
        link = list(set(member)-set(start))
        difference = abs(get_s(start) - get_s(link))
        answer = min(answer, difference)
print(answer)