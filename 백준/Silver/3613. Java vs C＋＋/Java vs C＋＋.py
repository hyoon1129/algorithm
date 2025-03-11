word = input()
java = True

upper = [chr(i)  for  i in range(ord("A"), ord("Z")+1)]
lower = [chr(i)  for  i in range(ord("a"), ord("z")+1)]


if "_" in word:
    for i in range(len(word)):
        if word[i] in upper:
            print("Error!")
            exit(0)
    java = False

if word[-1] == "_":
    print("Error!")
    exit(0)

if word[0] == "_":
    print("Error!")
    exit(0)

if word[0] in upper:
    print("Error!")
    exit(0)
    
if "__" in word:
    print("Error!")
    exit(0)


if not java:
    li = word.split('_')
    for i in range(len(li)):
        if i == 0:
            print(li[i], end = '')
        else:
            first = str(li[i][0])
            print(first.upper() + li[i][1:], end = '')
else:
    for i in range(len(word)):
        if word[i].isupper():
            print("_" + word[i].lower(), end = "")
        else:
            print(word[i], end = "")
