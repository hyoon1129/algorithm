def solution(name, yearning, photo):
    answer = []
    for li in photo:
        result = 0
        for nm in li :
            if nm in name:
                result += yearning[name.index(nm)]
        answer.append(result)
    return answer