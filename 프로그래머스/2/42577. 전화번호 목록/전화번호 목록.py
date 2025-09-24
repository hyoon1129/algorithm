def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)):
        num1 = phone_book[i]
        for j in range(i+1, len(phone_book)):
            num2 = phone_book[j]
            if num1 < num2[:len(num1)]:
                break
            elif num1 == num2[:len(num1)]:
                return False
    return True