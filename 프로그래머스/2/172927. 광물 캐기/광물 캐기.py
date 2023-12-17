# def solution(picks, minerals):
#     answer = 0
    
#     dia = {"dia":1, "iron":1, "stone":1}
#     iron = {"dia":5, "iron":1, "stone":1}
#     stone = {"dia":25, "iron":5, "stone":1}
    
#     for i in range(picks[0]*5):
#         if i >= len(minerals):
#             break
            
#         if minerals[i] == "diamond":
#             answer += dia["dia"]
#         elif minerals[i] == "iron":
#             answer += dia["iron"]
#         else:
#             answer += dia["stone"]
            
#     for i in range(picks[0]*5, picks[0]*5+picks[1]*5):
#         if i >= len(minerals):
#             break
            
        # if minerals[i] == "diamond":
        #     answer += iron["dia"]
        # elif minerals[i] == "iron":
        #     answer += iron["iron"]
        # else:
        #     answer += iron["stone"]
            
#     for i in range(picks[0]*5+picks[1]*5, sum(picks)*5):
#         if i >= len(minerals):
#             break
            
#         if minerals[i] == "diamond":
#             answer += stone["dia"]
#         elif minerals[i] == "iron":
#             answer += stone["iron"]
#         else:
#             answer += stone["stone"]
            
    
        
#     return answer

# def solution(picks, minerals):
    
#     answer = 0
    
#     global dia, iron, stone
    # dia = {"dia":1, "iron":1, "stone":1}
    # iron = {"dia":5, "iron":1, "stone":1}
    # stone = {"dia":25, "iron":5, "stone":1}
    
    
#     for i in range(picks[2]):
#         c = 10**9
#         for j in range(len(minerals)//5):
#             print(j)
#             new_cost = cost(2, minerals[j:j+5])
#             if c > new_cost:
#                 c = new_cost
#                 minerals = minerals[:i].append(minerals[i+5:])
            
            
            
# def cost(n, arr):
#     new_cost = 0
#     print(arr)
#     if n == 0:
#         for i in range(arr):
#             if arr[i] == "diamond":
#                 new_cost += dia["dia"]
#             elif arr[i] == "iron":
#                 new_cost += dia["iron"]
#             else:
#                 new_cost += dia["stone"]
#     elif n == 1:
#         for i in range(arr):
#             if arr[i] == "diamond":
#                 new_cost += iron["dia"]
#             elif arr[i] == "iron":
#                 new_cost += iron["iron"]
#             else:
#                 new_cost += iron["stone"]
#     else:
#         for i in range(arr):
#             if arr[i] == "diamond":
#                 new_cost += stone["dia"]
#             elif arr[i] == "iron":
#                 new_cost += stone["iron"]
#             else:
#                 new_cost += stone["stone"]
                
#     return new_cost

def solution(picks, minerals):
    answer = 0
    if sum(picks)*5 < len(minerals):
        minerals = minerals[:sum(picks)*5]
    
    cnt_min = [[0,0,0] for i in range(10)]
    
    
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            cnt_min[i//5][0] += 1
        elif minerals[i] == "iron":
            cnt_min[i//5][1] += 1
        else:
            cnt_min[i//5][2] += 1
    
    cnt_min = sorted(cnt_min, key = lambda x : (-x[0], -x[1], -x[2]))
    
    for i in range(3):
        for j in range(picks[i]):
            if len(cnt_min)<1:
                break
            d, ir, s = cnt_min[0]
            
            cnt_min = cnt_min[1:]
            
            # if len(cnt_min)>1:
            #     cnt_min = cnt_min[1:]
            # else:
            #     return answer
            
            if i == 0:
                answer += (d+ir+s)
            elif i == 1:
                answer += (d*5+ir+s)
            else:
                answer += (d*25+5*ir+s)
    return answer
                
            
        
    
    