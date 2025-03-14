import sys
input = sys.stdin.readline

n = int(input())
command = []
for i in range(n):
    command.append(list(map(int, input().split())))

stack = []

def c1(x):
    stack.append(x)
    return

def c2():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())
    return

def c3():
    print(len(stack))
    return

def c4():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
    return

def c5():
    if len(stack) != 0:
        print(stack[-1])
    else:
        print(-1)

for cmd in command:
    if cmd[0] == 1:
        c1(cmd[1])
    elif cmd[0] == 2:
        c2()
    elif cmd[0] == 3:
        c3()
    elif cmd[0] == 4:
        c4()
    else:
        c5()
