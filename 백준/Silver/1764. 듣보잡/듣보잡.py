n, m = map(int, input().split())

no_listen = {}
no_see = {}

for i in range(n):
    no_listen[input()] = 1

for i in range(m):
    no_see[input()] = 1
answer = no_listen.keys() & no_see.keys()

print(len(answer))
for name in sorted(answer):
    print(name)