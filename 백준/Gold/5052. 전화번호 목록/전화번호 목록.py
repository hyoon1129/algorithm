import sys
input = sys.stdin.readline


t = int(input())

def solution(li):
    li.sort()
    for i in range(len(li)-1):

        if li[i] == li[i+1][:len(li[i])]:
            return "NO"
    return "YES"

answer = []
for i in range(t):
    n = int(input())
    li = []
    for i in range(n):
        li.append(input().strip())
    answer.append(solution(li))

for a in answer:
    print(a)