from math import *

if __name__ == "__main__":
    a = input()
    b = a[: : -1]
    if gcd(int(a), int(b)) == 1:
        print('YES')
    else:
        print('NO')