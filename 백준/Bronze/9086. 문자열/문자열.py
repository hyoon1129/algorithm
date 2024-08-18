import sys

t = int(input())
li = []

for i in range(t):
    li.append(input())

answer = []

for s in li:
    print(s[0]+s[-1])