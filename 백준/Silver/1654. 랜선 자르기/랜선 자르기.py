k, n = map(int, input().split()) # k개의 랜선을 잘라서 같은 길이로 n개 이상 만들기

li = []
for i in range(k):
    li.append(int(input()))

start, end = 1, max(li)

def get_cnt(num):
    result = 0
    for i in range(k):
        result += li[i] // num
    return result

while start <= end :
    mid = (start + end) // 2

    if get_cnt(mid) >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)