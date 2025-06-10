n = int(input())
pattern = input()

files = []
for i in range(n):
    files.append(input())

idx = pattern.index("*")
prefix = pattern[:idx]
suffix = pattern[idx+1:]


for file in files:
    if len(file) < len(pattern)-1:
        print("NE")
    elif not file.startswith(prefix) or not file.endswith(suffix):
        print("NE")
    else:
        print("DA")