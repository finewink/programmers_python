def solution(prices):
    answer = []
    temp = 0
    for i, item in enumerate(prices) : 
        for j in range(i + 1 , len(prices)) :
            temp += 1
            if prices[j] >= item:
                pass
            else :
                break
        answer.append(temp)
        temp = 0
    return answer