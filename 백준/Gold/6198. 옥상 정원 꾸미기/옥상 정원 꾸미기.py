n = int(input())
stack = []
result = 0

for _ in range(n):
    height = int(input())

    while stack and stack[-1] <= height:
        stack.pop()
    result += len(stack)
    stack.append(height)
print(result)