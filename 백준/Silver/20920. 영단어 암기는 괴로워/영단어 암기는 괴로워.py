n, m = map(int, input().split())

words = {}

for i in range(n):
    word = input()
    if len(word) >= m:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
result = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in range(len(result)):
    print(result[i][0])