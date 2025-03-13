t = int(input())

def get_fox():
    sound = list(map(str, input().split()))

    dic = {}

    for i in range(100):
        s = input()
        if s == "what does the fox say?":
            break
        animal, a_sound = s.split(" goes ")
        dic[a_sound] = animal

    answer = ""
    for i in range(len(sound)):
        if sound[i] not in dic:
            answer += sound[i]
            answer += " "

    print(answer.strip())

for i in range(t):
    get_fox()