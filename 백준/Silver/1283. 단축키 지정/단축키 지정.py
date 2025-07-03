n = int(input())
options = [input() for _ in range(n)]
used = set()

for option in options:
    words = option.split()
    found = False

    # 1단계: 각 단어의 첫 글자 확인
    for idx, word in enumerate(words):
        ch = word[0].lower()
        if ch not in used:
            used.add(ch)
            words[idx] = f"[{word[0]}]{word[1:]}"
            print(" ".join(words))
            found = True
            break

    if found:
        continue

    # 2단계: 문장 전체에서 순차적으로 탐색
    for i, ch in enumerate(option):
        if ch == ' ':
            continue
        if ch.lower() not in used:
            used.add(ch.lower())
            print(option[:i] + "[" + ch + "]" + option[i+1:])
            found = True
            break

    if not found:
        print(option)
