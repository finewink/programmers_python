def solution(numbers):
    answer = 0

    combi = set()

    prifix = ''

    for i in range(len(numbers)) :
        get_combi(numbers[:], combi, i, 0)

    prime = []

    for v in combi:
        if is_prime(v) :
            prime.append(v)
            answer += 1

    print(sorted(combi))
    print(prime)
    return answer

def get_combi(numbers, combi, l, d) :
    if d >= len(numbers) :
        return
    
    combi.add(int(numbers[0:l + 1]))

    for idx in range(d, len(numbers)) :
        numbers = swap(numbers, d, idx)    
        get_combi(numbers, combi, l, d + 1)

def swap(numbers, i, k) : 
    lnum = list(numbers[:])

    temp = lnum[k]
    lnum[k] = lnum[i]
    lnum[i] = temp

    return "".join(lnum)

def is_prime(k) :
    if k < 2 :
        return False
    i = 2
    while i * i <= k :
        if is_prime(i) :
            if k % i == 0 :
                return False
        i += 1

    return True