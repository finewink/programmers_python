def solution(array, commands):
    answer = []

    for op in commands :
        answer.append(sorted(array[op[0] - 1 : op[1]].copy())[op[2] - 1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
#return list(map(lambda op : sorted(array[op[0] - 1 : op[1]].copy())[op[2] - 1], commands))