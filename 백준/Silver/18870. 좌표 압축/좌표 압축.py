import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

sorted_li = sorted(list(set(li))) # 중복이 제거되고 sort된 리스트
dic = {}

for i in range(len(sorted_li)):
    dic[sorted_li[i]] = i # 딕셔너리에 각 원소 index 저장

for i in li:
    print(dic[i])