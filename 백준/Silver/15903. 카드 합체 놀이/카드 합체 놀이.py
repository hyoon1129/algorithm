import heapq

n, m = map(int, input().split())

card = list(map(int, input().split()))
heapq.heapify(card)

for i in range(m):
    a, b = heapq.heappop(card), heapq.heappop(card)
    new = a + b
    heapq.heappush(card, new)
    heapq.heappush(card, new)
print(sum(card))