import math

def solution(numbers):    
    return max(numbers) == 0 and "0" or "".join(map(lambda k : str(k), sorted(numbers, key=lambda k : (str(k) * math.ceil(6/len(str(k))))[:6], reverse = True)))
    