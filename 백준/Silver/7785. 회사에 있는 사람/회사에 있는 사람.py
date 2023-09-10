import sys
input = sys.stdin.readline

n= int(input())

log_dic = {}
for i in range(n):
    name, log = input().split()
    if log == 'enter':
        log_dic[name] = 1
    else:
        del log_dic[name]

li = sorted(log_dic.keys(), reverse = True)

for k in li:
    print(k)