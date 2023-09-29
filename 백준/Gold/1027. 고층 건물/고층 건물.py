import sys
input = sys.stdin.readline

n = int(input())
building = list(map(int, input().split()))
dict = {}

for i in range(1,n+1):
    if n == 1:
        dict[i] = 0
        break
    if i == 1:
        dict[i] = 1
    elif i == n :
        dict[i] = 1
    else:
        dict[i] = 2

max_inclination = 0

def inclination(a,b):
    return (b[1] - a[1]) / (b[0] - a[0])


def see(a,b):
    for i in range(a[0] + 1, b[0]):

        if max_inclination <= inclination(a, [i, building[i-1]]):
            break
        if i == b[0] - 1:
            dict[a[0]] += 1
            dict[b[0]] += 1

for i in range(1, n+1):
    a = [i, building[i - 1]]
    for j in range(i+2, n+1):
        b = [j, building[j-1]]
        max_inclination = inclination(a,b)
        see(a, b)

all_values = dict.values()
max_value = max(all_values)
print(max_value)

