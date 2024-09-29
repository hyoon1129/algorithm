def solution(n):
    answer = 0
    bin_n = format(n,'b')
    cnt = bin_n.count("1")
    
    start = n + 1
    while True:
        if format(start,"b").count("1") == cnt:
            return start
        start += 1

    
    
    
    



# def solution(n):
#     answer = 0
#     bin_n = format(n,'b')
#     cnt = bin_n.count('1')
#     while True:
#         n += 1
#         a = format(n, 'b')
#         if a.count('1') == cnt:
#             return n