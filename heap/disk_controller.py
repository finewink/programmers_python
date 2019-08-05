from collections import deque

def solution(jobs) :
    time = 0
    total = 0
    job = []

    queue = sorted(deque(jobs), key=lambda k: k[1])

    while queue :
        for i, item in enumerate(queue) :
            if item[0] <= time :
                job = queue.pop(i)
                time += job[1]
                total += time - job[0]
                break
        if not job :
            time += 1
            continue
        
        job = None
        
    return int(total / len(jobs))

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))