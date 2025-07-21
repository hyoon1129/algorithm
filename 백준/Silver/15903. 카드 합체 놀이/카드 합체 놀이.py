n, m = map(int, input().split())

card = sorted(list(map(int, input().split())))

for i in range(m):
    new = card[0]+card[1]
    card[0], card[1] = new, new
    card.sort()
print(sum(card))