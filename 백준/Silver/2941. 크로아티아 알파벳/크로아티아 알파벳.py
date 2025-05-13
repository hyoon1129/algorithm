li = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()

for word in li:
    s = s.replace(word, ".")

print(len(s))