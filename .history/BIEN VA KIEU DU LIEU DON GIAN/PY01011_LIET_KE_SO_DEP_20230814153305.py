def check(n):
    qhoa = str(n)
    qhoa1 = qhoa[:]
    qhoa2 = qhoa[: : -1]
    print(qhoa1, qhoa)
    cnt = 0
    a = [0, 2, 4, 6, 8]
    while n != 0:
        tmp = n % 10
        cnt += 1
        if tmp not in a:
            return False
        n //= 10
    return cnt % 2 == 1 and qhoa1 == qhoa2

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = int(input())
        for i in range(n):
            # if check(i):
            #     print(i, end = ' ')
        t -= 1
        print()