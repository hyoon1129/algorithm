n = int(input())

dic = {"ChongChong"}

for i in range(n):
    a, b = map(str, input().split())
    if a in dic:
        dic.add(b)
    if b in dic:
        dic.add(a)
print(len(dic))