import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    item_1 = 0
    item_2 = 0
    last_item = 0

    while scoville :
        item_1 = heapq.heappop(scoville)
        last_item = item_1
        if scoville :
            item_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, item_1 + item_2 * 2)
            last_item = scoville[0]
            answer += 1
        
        if(last_item >= K):
            break
    else :
        if(last_item < K):
            answer = -1
    return answer