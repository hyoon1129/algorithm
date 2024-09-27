def solution(data, ext, val_ext, sort_by):
    answer = []
    
    ext_idx = idx_num(ext)
    
    for d in data:
        if d[ext_idx] < val_ext:
            answer.append(d)
    
    sort_idx = idx_num(sort_by)
    
    answer.sort(key = lambda x:x[sort_idx])
    return answer

def idx_num(s):
    if s == "code":
        return 0
    elif s == "date":
        return 1
    elif s == "maximum":
        return 2
    else:
        return 3