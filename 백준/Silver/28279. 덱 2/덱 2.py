from collections import deque
n = int(input())

command = []
queue = deque()

for i in range(n):
    command.append(input())

def check_deque(queue):
    if len(queue) == 0:
        return False
    return True

for c in command:
    if c[0] == "1":
        _, value = c.split()
        queue.appendleft(value)
    elif c[0] == "2":
        _, value = c.split()
        queue.append(value)
    elif c == "3":
        if check_deque(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif c == "4":
        if check_deque(queue):
            print(queue.pop())
        else:
            print(-1)
    elif c == "5":
        print(len(queue))
    elif c == "6":
        if check_deque(queue):
            print(0)
        else:
            print(1)
    elif c == "7":
        if check_deque(queue):
            print(queue[0])
        else:
            print(-1)
    else:
        if check_deque(queue):
            print(queue[-1])
        else:
            print(-1)