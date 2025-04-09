n, c = map(int, input().split())
li = list(map(int, input().split()))

dic = {}
order = [] # 등장 순서

for num in li:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
        order.append(num)

sorted_li = sorted(dic.items(), key= lambda x: (-x[1], order.index(x[0])))

for i in range(len(dic)):
    for j in range(sorted_li[i][1]):
        print(sorted_li[i][0], end = " ")