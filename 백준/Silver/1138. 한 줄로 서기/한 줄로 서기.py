n = int(input())

li = list(map(int, input().split()))

answer = [0] * n


for i in range(n):
    cnt = 0
    for j in range(n):
        if answer[j] == 0:
            if cnt == li[i]:
                answer[j] = i+1
                break
            cnt += 1

print(*answer)