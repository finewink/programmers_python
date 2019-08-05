from collections import deque

def solution(operations):
    answer = []

    queue = deque()
     
    op = ''
    operand = 0
    for item in operations :
        op = item[:1]
        operand = int(item[1:])
        if op == 'I' :
            queue.append(operand)
        elif op == 'D' and not queue :
            pass
        elif op == 'D' and operand > 0:
            queue = deque(sorted(queue, reverse = True))
            queue.popleft()
        else:
            queue = deque(sorted(queue, reverse = True))
            queue.pop()
    
    queue = deque(sorted(queue, reverse = True))

    if queue :
        answer.append(queue.popleft())
        if queue:
            answer.append(queue.pop())
        else:
            answer = [0, 0]
    else:
        answer = [0, 0]

    return answer