from itertools import permutations
n, m = map(int, input().split())

li = list(map(int, input().split()))
li.sort()


for p in permutations(li, m):
    print(" ".join(map(str, p)))