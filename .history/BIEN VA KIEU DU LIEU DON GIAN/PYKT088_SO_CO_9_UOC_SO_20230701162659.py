from math import *

def Ptich(n):
    res = 1
    for i in range(2, isqrt(n) + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt != 0:
            res *= (cnt + 1)
    if n != 1:
        res *= 2
    return res

if __name__ == '__main__':
    
