import sys
input = sys.stdin.readline

from collections import deque

def solution(n, tree):

    q = deque([1])
    answer = [0] * (n+1)
    while q:
        node = q.popleft()
        for i in tree[node]:
            if answer[i] == 0 and i != 1:
                answer[i] = node
                q.append(i)
    for i in answer[2:]:
        print(i)



n = int(input())
dic = {}
for i in range(n-1):
    a, b = map(int, input().split())

    if a in dic :
        dic[a].append(b)
    else:
        dic[a] = [b]

    if b in dic :
        dic[b].append(a)
    else:
        dic[b] = [a]

solution(n, dic)