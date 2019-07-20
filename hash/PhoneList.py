def solution(phone_book) :
    answer = True

    phone_book.sort()

    for x in phone_book :
        newBook = set(str(i)[:len(str(x))] for i in phone_book if i > x)
        if str(x) in newBook:
            return False

    return answer

phone_book = [119, 97674223, 1195524421]
answer = solution(phone_book)
print(answer)