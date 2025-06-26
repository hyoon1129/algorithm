n, game = map(str, input().split())
n = int(n)

name = set()

for i in range(n):
    name.add(input())

l = len(name)

if game == "Y":
    print(l)
elif game == "F":
    print(l//2)
else:
    print(l//3)