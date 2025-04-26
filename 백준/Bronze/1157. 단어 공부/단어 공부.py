word = input()
word = word.upper()

dic = {}

for i in range(len(word)):
    if word[i] in dic:
        dic[word[i]] += 1
    else:
        dic[word[i]] = 1

tmp = [k for k, v in dic.items() if max(dic.values()) == v]

if len(tmp) > 1:
    print("?")
else:
    print(tmp[0])