word = input()
results = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        part1 = word[:i][::-1]
        part2 = word[i:j][::-1]
        part3 = word[j:][::-1]

        results.append(part1+part2+part3)
print(min(results))