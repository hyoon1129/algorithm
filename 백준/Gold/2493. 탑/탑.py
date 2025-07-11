n = int(input())

towers = list(map(int, input().split()))

answer = [0 for _ in range(n)]

stack = []
for i in range(n):
    height = towers[i]

    while stack and stack[-1][1] < height:
        stack.pop()
    if stack:
        answer[i] = stack[-1][0] + 1

    stack.append((i, height))

print(*answer)