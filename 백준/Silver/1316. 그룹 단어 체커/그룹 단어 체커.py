n = int(input())


answer = 0

def solution(word):
    dic = {}
    dic[word[0]] = 1
    for i in range(1, len(word)):
        if word[i] != word[i-1] and word[i] in dic:
            return False
        if word[i] not in dic:
            dic[word[i]] = 1
    else:
        return True

for i in range(n):
    word = input()
    if solution(word):
        answer += 1

print(answer)