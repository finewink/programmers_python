def solution(N, number):
    calc = [plus, minus, r_minus, multiple, div, r_div]
    res = [{0},{N}]
    cnt = 2
    while cnt <= 8 :
        cal_set = set()
        times = int(str(N) * (cnt))
        cal_set.add(times)
        if times == number :
            return cnt
        else :
            for idx in range(1, int(cnt/2) + 1) :    
                for item1 in res[cnt - idx] :
                    for item2 in res[idx] :
                        for cal in calc :
                            val = cal(item1, item2)
                            if val == number :
                                return cnt
                            cal_set.add(val)

            res.append(cal_set)
            cnt += 1
    return -1

def plus(x, y) :
    return x + y

def minus(x, y) :
    return x - y

def r_minus(x, y) :
    return y - x

def multiple(x, y) :
    return x * y

def div(x, y) :
    if y != 0 :
        return x // y
    else :
        return 0

def r_div(x, y) :
    if x != 0 :
        return y // x
    else :
        return 0