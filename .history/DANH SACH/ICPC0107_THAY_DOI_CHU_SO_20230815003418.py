if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        p, q = map(int, input().split())
        a = list(map(int, input().split()))
        if len(a) == 1:
            x1 = a[0]
            x2 = int(input())
        else:
            x1, x2 = a[0], a[1]
        small1, small2 = s1.replace(y, x), s2.replace(y, x)
        big1, big2 = s1.replace(x, y), s2.replace(x, y)
        print(int(small1) + int(small2), int(big1) + int(big2))