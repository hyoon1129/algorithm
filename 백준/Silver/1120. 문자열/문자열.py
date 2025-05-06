a, b = map(str, input().split())

def get_diff(x, y):
    result = 0
    for i in range(len(y)):
        if x[i] != y[i]:
            result += 1
    return result

answer = 10**9
for i in range(len(b)-len(a)+1):
    answer = min(get_diff(a, b[i:i+len(a)]), answer)

print(answer)