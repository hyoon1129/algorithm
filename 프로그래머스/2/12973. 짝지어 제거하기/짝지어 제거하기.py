def solutio(s):
    li = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll',
          'mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
    i = 0
    while i < 26:
        for k in range(0,26):
            s = s.replace(li[k], '')
        i += 1
    if len(s)>=1:
        return 0
    else:
        return 1
    #이건 왜 안돼
    
def solution(s):
    stack = []
    stack.append(s[0])
    for i in range(1,len(s)):
        if stack == []:
            stack.append(s[i])
        else:
            stack.append(s[i])
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    if stack == []:
        return 1
    else:
        return 0