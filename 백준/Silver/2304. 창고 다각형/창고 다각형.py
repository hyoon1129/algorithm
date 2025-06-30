n = int(input())


pillars = [tuple(map(int, input().split())) for _ in range(n)]
pillars.sort()

max_height = max(pillars, key=lambda x:x[1])[1]
max_indices = [i for i, (x,h) in enumerate(pillars) if h == max_height]

area = 0

# 왼쪽에서 첫 번째 최대 높이까지
left_max = 0
prev_x = pillars[0][0]

for i in range(max_indices[0] + 1):
    x, h  = pillars[i]
    if h >= left_max:
        if i > 0:
            area += (x-prev_x) * left_max
        left_max = h
        prev_x = x

# 오른쪽에서 마지막 최대 높이까지
right_max = 0
prev_x = pillars[-1][0]

for i in range(len(pillars)-1, max_indices[-1]-1, -1):
    x, h = pillars[i]
    if h >= right_max:
        if i < len(pillars) - 1:
            area += (prev_x - x) * right_max
        right_max = h
        prev_x = x

# 최대 높이 구간
max_x_positions = [pillars[i][0] for i in max_indices]
center_area = (max(max_x_positions) - min(max_x_positions) + 1) * max_height

print(area + center_area)