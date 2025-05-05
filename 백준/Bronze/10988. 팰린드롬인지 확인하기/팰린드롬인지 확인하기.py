word = input()

for i in range(len(word)//2):
    if word[i] != word[len(word)-i-1] :
        print(0)
        exit()
    else:
        continue
print(1)