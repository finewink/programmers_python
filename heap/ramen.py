import heapq

def solution(stock, dates, supplies, k):
    answer = 0

    merged = list(zip([-k for k in supplies], dates)) # max_heap
    heapq.heapify(merged)

    curr_stock = stock
    curr_date = 0
    
    wait = []

    while merged : 
        s, d = heapq.heappop(merged) # top을 꺼냄
        
        if curr_stock - curr_date >= d - curr_date: #재고 소진 시까지 날짜보다 입고일이 빨라야 함
            curr_stock += -s # 음수변환된 supplies반전
            curr_date += d
            answer += 1
            while wait :
                heapq.heappush(merged, wait.pop())
        else :
            wait.append((s, d))

        if curr_stock >= k :
            break

    return answer


stock = 4
dates = [4,10,15]
supplies = [20,5,10]	
k = 30

print(solution(stock, dates, supplies, k))