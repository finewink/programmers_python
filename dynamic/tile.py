def solution(N):
    return calc(1, 1, 1, N)

def calc(x, y, cnt, N) :
    if cnt == N :
        return x * 2 + y * 2
    else :
        return calc(y, x + y, cnt + 1, N)