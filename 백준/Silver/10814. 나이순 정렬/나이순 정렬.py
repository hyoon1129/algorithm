n = int(input())
user = []

for i in range(n):
    age, name = map(str, input().split())
    user.append([int(age), name, i])

user.sort(key= lambda x: (x[0], x[2]))

for i in range(n):
    print(user[i][0], user[i][1])
