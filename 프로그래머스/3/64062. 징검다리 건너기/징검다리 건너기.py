def solution(stones, k):
    answer = 0
    
    if len(stones) == 1:
        return stones[0]
    
#     min_stone = min(stones)

    
#     for i in range(len(stones)):
#         stones[i] -= min_stone
        
#     answer += min_stone
    
#     while "0"*k not in ''.join(str(s) for s in stones):
#         min_stone = sorted(set(stones))[1]
#         for i in range(len(stones)):
#             stones[i] = max(0, stones[i]-min_stone)
#         answer += min_stone

    start = min(stones)
    end = max(stones)
    
    while start <= end:
        mid = (start+end)//2
        
        cnt = 0
        for i in range(len(stones)):
            if stones[i] <= mid:
                cnt += 1
                if cnt >= k:
                    end = mid - 1
                    answer = mid
                    break
            else:
                cnt = 0
        else:
            start = mid + 1
            
                
            
        
#         # if "0"*k in ''.join(str(s) for s in stone):
#         #     end = mid - 1
#         #     answer = mid
#         # else:
#         #     start = mid + 1
#         cnt = 0
#         for i in range(len(stone)):
#             if stone[i] <= 0:
#                 cnt += 1
#                 if cnt >= k:
#                     # end = mid - 1
#                     # answer = mid
#                     break
#             else:
#                 cnt = 0
#         # else:
#         #     start = mid + 1
#         if cnt >= k:
#             end = mid - 1
#             answer = mid
#         else:
#             start = mid + 1
                
        
        
    return answer

# 이분탐색?
# 최솟값 : 1, 최댓값 : max(stones)
# mid명만큼 건넜을 때 