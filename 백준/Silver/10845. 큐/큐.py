from collections import deque
n = int(input())

queue = deque()

def not_empty(q):
    if len(q) == 0:
        return False
    return True

for i in range(n):
    command = input()

    if command[:4] == "push":
        queue.append(int(command.split()[1]))
    elif command == "pop":
        if not_empty(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if not_empty(queue):
            print(0)
        else:
            print(1)
    elif command == "front":
        if not_empty(queue):
            print(queue[0])
        else:
            print(-1)
    elif command == "back":
        if not_empty(queue):
            print(queue[-1])
        else:
            print(-1)