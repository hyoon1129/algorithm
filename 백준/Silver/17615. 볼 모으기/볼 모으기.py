n = int(input())
balls = input()

if 'R' not in balls or 'B' not in balls:
    print(0)
    exit()

result = []

# 빨강을 왼쪽으로
idx = 0
for i in range(len(balls)):
    if balls[i] == 'B':
        idx = i
        break

result.append(balls[idx:].count('R'))

# 빨강을 오른쪽으로
idx = 0
for i in range(1, len(balls)+1):
    if balls[-i] == 'B':
        idx = -i
        break
result.append(balls[:idx].count('R'))

# 파랑을 왼쪽으로
idx = 0
for i in range(len(balls)):
    if balls[i] == 'R':
        idx = i
        break

result.append(balls[idx:].count('B'))

# 파랑을 오른쪽으로
idx = 0
for i in range(1, len(balls)+1):
    if balls[-i] == 'R':
        idx = -i
        break
result.append(balls[:idx].count('B'))

print(min(result))