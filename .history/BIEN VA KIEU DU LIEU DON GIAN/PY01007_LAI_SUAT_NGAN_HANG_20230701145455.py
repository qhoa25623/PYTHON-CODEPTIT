if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n, x, m = map(float, input().split())
        res = 0
        while n < m:
            n += n * 0.1
            res += 1
        print(res)
        t -= 1
