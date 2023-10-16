import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
num = [i for i in range(1,n+1)]

for i in list(permutations(num, m)):
    for j in range(len(i)):
        print(i[j], end = ' ')
    print("")
