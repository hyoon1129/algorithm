n, m = map(int,input().split())

dic = {}
for i in range(n):
    site, password = input().split()
    dic[site] = password
    
for j in range(m):
    print(dic[input()])