def solution(genres, plays):
    answer = []
    genre_cnt = {} # {장르1 : 장르1이 재생된 총 횟수}
    temp = {} # {장르1 : [[곡번호, 재생횟수], []], 장르2: ... }
    
    for i in range(len(genres)):
        if genres[i] not in genre_cnt:
            genre_cnt[genres[i]] = plays[i]
        else:
            genre_cnt[genres[i]] += plays[i]
            
    for i in range(len(plays)):
        if genres[i] not in temp:
            temp[genres[i]] = []
            temp[genres[i]].append([i, plays[i]])
        else:
            temp[genres[i]].append([i, plays[i]])
            
    genre_cnt = list(sorted(list(genre_cnt.items()), key= lambda item:item[1], reverse = True))
            
    
    for i in range(len(genre_cnt)):
        li = temp[genre_cnt[i][0]]
        li = sorted(li, key = lambda x : (-x[1], x[0]))
        if len(li)>=2:
            for j in range(2):
                answer.append(li[j][0])
        else:
            for j in range(len(li)):
                answer.append(li[j][0])
    return answer