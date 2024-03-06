def solution(book_time):
    answer = 0

    for t in book_time:
        t[0] = minute(t[0])
        t[1] = minute(t[1])
    
    book_time.sort(key = lambda x : x[0])
    
    room = []
    
    for book in book_time:
        for i in range(len(room)):
            if book[0] >= room[i] + 10 and book[1] <= minute("23:59"):
                room[i] = book[1]
                break
        else:
            room.append(book[1])
                
        room.sort()
    
    
    return len(room)

def minute(s):
    return int(s[:2])*60 + int(s[-2:])