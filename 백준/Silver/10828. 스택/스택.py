n = int(input())

stack = []

for i in range(n):
    cmd = input()

    if cmd == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif cmd == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(int(cmd[5:]))