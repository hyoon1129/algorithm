n= int(input())
nlist = list(map(int,input().split()))
m = n= int(input())
mlist = list(map(int,input().split()))

nlist = sorted(list(set(nlist)))

ndic = {}
for i in nlist:
    ndic[i] = 1

for i in mlist:
    if i in ndic:
        print(1)
    else:
        print(0)