from math import *
prime = [True] * (10 ** 6 + 1)

def sieve():
    prime[0], prime[1] = False, False
    for i in range(2, isqrt(10 ** 6) + 1):
        if prime[i]:
            for j in range(i * i, 10 ** 6 + 1, i):
                prime[j] = False
if __name__ == "__main__":
    sieve()
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if prime[a[i][j]]:
                print(1, end = ' ')