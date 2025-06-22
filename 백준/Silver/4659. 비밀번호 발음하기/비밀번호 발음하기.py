def check(password):
    vowels = 'aeiou'
    has_vowel = False
    vowel_count = 0
    consonant_count = 0
    prev = ''
    
    for c in password:
        if c in vowels:
            has_vowel = True
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0
        
        if vowel_count >= 3 or consonant_count >= 3:
            return False
        
        if prev == c and c not in 'eo':
            return False
        
        prev = c
    
    return has_vowel

while True:
    pw = input()
    if pw == 'end':
        break
    
    if check(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")