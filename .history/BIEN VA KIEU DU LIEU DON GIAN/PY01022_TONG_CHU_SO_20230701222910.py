if __name__ == "__main__":
    n = int(input())
    n = abs(n)
    cnt = 0
    while n > 9:
        cnt += 1
        sum = 0
        while n != 0:
            sum += n % 10
            n //= 10
        n = sum
    print(cnt)
