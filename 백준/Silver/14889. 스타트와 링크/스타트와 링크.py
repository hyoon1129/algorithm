from itertools import combinations

n = int(input())

matrix = []


for _ in range(n):
    matrix.append(list(map(int, input().split())))

total = 0

for i in range(n):
    total += sum(matrix[i])

members = [i for i in range(n)]

answer = 10**9
visited = []

for start_team in combinations(members, n//2):
    start, link = 0, 0
    link_team = [x for x in members if x not in start_team]

    for a in start_team:
        for b in start_team:
            start += matrix[a][b]
            start += matrix[b][a]
    for a in link_team:
        for b in link_team:
            link += matrix[a][b]
            link += matrix[b][a]

    answer = min(abs(start-link), answer)

print(answer//2)