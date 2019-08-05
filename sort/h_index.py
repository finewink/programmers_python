def solution(citations):
    answer = 0

    citations.sort()

    for i, v in enumerate(citations) :
        for k in range(v, 0, -1) :
            len_gt = len(citations[i:])
            len_lt = len(citations[:i])
            if len_gt >= k and len_lt < k :
                if answer < k :
                    answer = k

    return answer