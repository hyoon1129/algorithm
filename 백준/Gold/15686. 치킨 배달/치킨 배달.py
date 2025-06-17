from itertools import combinations
n, m = map(int, input().split())
city = []

for i in range(n):
    city.append(list(map(int, input().split())))

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

result = 10**9
for combi in combinations(chickens, m):
    city_distance = 0
    for hx, hy in houses:
        distance = min(abs(hx-cx) + abs(hy-cy) for cx, cy in combi)
        city_distance += distance
    result = min(result, city_distance)

print(result)