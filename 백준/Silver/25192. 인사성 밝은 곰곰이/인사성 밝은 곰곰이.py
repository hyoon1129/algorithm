n = int(input())

answer = 0
name = set()
for i in range(n):
    new = input()
    if new == "ENTER":
        answer += len(name)
        name = set()
    else:
        name.add(new)

answer += len(name)
print(answer)