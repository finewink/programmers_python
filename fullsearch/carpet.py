def solution(brown, red):
    answer = []
    
    x = 1
    y = 1

    while y <= red :
        while x * y <= red :
            if x * y == red and x >= y:
                outer = (x + 2) * 2 + (y) * 2
                if outer == brown :
                    return [x + 2, y + 2]
            x += 1
        y += 1
        x = 1
            
    return answer