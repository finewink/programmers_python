import collections

def solution(priorities, location):
    answer = 0
    

    queue = collections.deque(range(len(priorities)))
    while queue :
        index  = queue.popleft()
        exists = False
        for i in queue :
            if priorities[index] < priorities[i] :        
                queue.append(index)
                exists = True
                break
            else :
                exists = False
        if not exists :
            answer += 1
            if index == location : 
                break

    return answer