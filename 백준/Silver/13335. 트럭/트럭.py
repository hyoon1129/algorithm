from collections import deque
n, w, l = map(int, input().split()) # 트럭 수, 다리 길이, 최대하중

trucks = deque(map(int, input().split()))

bridge = deque([0 for _ in range(w)])


time = 0

while trucks:
    bridge.popleft()
    if sum(bridge) + trucks[0] <= l:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)
    time += 1

while sum(bridge) > 0:
    bridge.popleft()
    bridge.append(0)
    time += 1
print(time)