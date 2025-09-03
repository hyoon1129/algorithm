n = int(input())
li = [int(input()) for _ in range(n)]

stack = []
current = 1
result = []
for num in li:
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit()

for op in result:
    print(op)