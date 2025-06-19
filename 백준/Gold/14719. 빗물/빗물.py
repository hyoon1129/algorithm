h, w = map(int, input().split())

block = list(map(int, input().split()))

left_max = [0] * w
right_max = [0] * w

left_max[0] = block[0]
for i in range(1, w):
    left_max[i] = max(left_max[i-1], block[i])

right_max[-1] = block[-1]
for i in range(w-2, -1, -1):
    right_max[i] = max(right_max[i+1], block[i])

answer = 0
for i in range(w):
    answer += min(left_max[i], right_max[i]) - block[i]

print(answer)