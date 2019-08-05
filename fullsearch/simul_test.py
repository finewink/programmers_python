import math
def solution(answers):
    answer = []

    stu_1 = (list(i + 1 for i in range(5)) * math.ceil(len(answers) / 5))[:len(answers)]
    stu_2 = ([2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(len(answers) / 8))[:len(answers)]
    stu_3 = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(len(answers) / 10))[:len(answers)]
    correct = [0, 0, 0]
    
    for k in zip(answers, stu_1, stu_2, stu_3) :
        for i, v in enumerate(k[1:]) :
            if k[0] == v :
                correct[i] += 1

    max_score = max(correct)
    for i, v in enumerate(correct) :
        if v == max_score:
            answer.append(i + 1)

    return answer

answers = [1,2,3,4,5, 2]
print(solution(answers))