from collections import deque
t = int(input())

def solution(s):
    queue = deque()
    for p in s:
        if len(queue) == 0:
            queue.append(p)
        elif queue[-1] == '(' and p == ')':
            queue.pop()
        else:
            queue.append(p)
    if len(queue) != 0:
        return False
    return True

for i in range(t):
    s = input()
    if solution(s):
        print('YES')
    else:
        print('NO')