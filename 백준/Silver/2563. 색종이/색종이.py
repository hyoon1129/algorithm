num = int(input())

li = []
paper = [[0] * 100 for i in range(100)]
for i in range(num):
    li.append(list(map(int, input().split())))

for i in range(num):
    a, b = li[i]
    for j in range(a, a+10):
        for k in range(b, b+10):
            paper[j][k] = 1

answer = 0
for i in range(100):
    answer += paper[i].count(1)
print(answer)