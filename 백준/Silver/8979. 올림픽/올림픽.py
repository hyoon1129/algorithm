n, k = map(int, input().split())

medals = []

for _ in range(n):
    medals.append(list(map(int, input().split())))

medals = sorted(medals, key = lambda x: (-x[1], -x[2], -x[3]))

rank = 1
prev = medals[0][1:]

rank_dic = {medals[0][0] : 1}

for i in range(1, n):
    now = medals[i][1:]

    if now != prev:
        rank = i+1
    rank_dic[medals[i][0]] = rank
    prev = now

print(rank_dic[k])