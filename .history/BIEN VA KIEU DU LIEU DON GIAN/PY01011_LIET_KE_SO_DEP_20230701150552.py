def even(n):
    while n != 0:
        tmp = n % 10
        if tmp % 2 != 0:
            return False
        n //= 10
    return True

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        n = int(input())
