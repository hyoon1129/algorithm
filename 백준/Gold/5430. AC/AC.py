from collections import deque
# R : 베열 순서 뒤집기
# D : 첫 번째 수 버리기

t = int(input())

def solution():
    p = input()
    n = int(input())
    li = input()
    li = li[1:-1]

    if len(li) == 0:
        queue = deque()
    else:
        queue = deque(map(int, li.split(",")))

    reverse = False

    for func in p:
        if func == "R":
            reverse = not reverse
        else:
            if len(queue) == 0:
                return "error"
            if reverse:
                queue.pop()
            else:
                queue.popleft()
    if reverse:
        queue.reverse()

    return "[" + ",".join(map(str, queue)) + "]"

for i in range(t):
    print(solution())
