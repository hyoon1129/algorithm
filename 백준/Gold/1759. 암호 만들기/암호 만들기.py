import sys
input = sys.stdin.readline
from itertools import combinations

l, c = map(int, input().split())
li = list(map(str, input().split()))
li.sort()


consonant = 'qwrtypsdfghjklzxcvbnm'
vowel = 'aeiou'


def consonant_count(code):
    cnt = 0
    for i in code:
        if i in consonant:
            cnt += 1
    return cnt

def vowel_count(code):
    cnt = 0
    for i in code:
        if i in vowel:
            cnt += 1
    return cnt

for code in list(map(''.join, combinations(li, l))):
    if vowel_count(code)>=1 and consonant_count(code)>=2:
        print(str(code))