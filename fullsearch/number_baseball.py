def solution(baseball):
    answer = 0

    pos = set()
    baseball.sort(key=lambda k : (k[1], k[2]), reverse = True)

    for i in range(123, 987 + 1) :         
        tgt = str(i)
        if "0" in tgt:
            continue
        if tgt[0] == tgt[1] or tgt[1] == tgt[2] or tgt[0] == tgt[2]:
            continue

        if is_pos(baseball, i) :
            answer += 1

    return answer

def is_pos(baseball, num) :
    chk = list(str(num))

    for item in baseball :
        if "0" in str(item[0]) :
            return False
        if item[1] != get_strike(item[0], chk) or item[2] != get_ball(item[0], chk):
            return False
        
    return True

def get_strike(origin, chk) :
    strike = 0
    for i in zip(str(origin), chk) :
        if i[0] == i[1] :
            strike += 1

    return strike

def get_ball(origin, chk) :
    ball = 0
    for i, v in enumerate(str(origin)) :
        for idx, s in enumerate(chk) :
            if i != idx and v == s :
                ball += 1
                
    return ball