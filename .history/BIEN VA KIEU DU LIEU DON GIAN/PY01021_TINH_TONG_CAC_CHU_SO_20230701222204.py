if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        a = []
        sum = 0
        for i in range(len(s)):
            if s[i].isalpha():
                a.append(s[i])
            else:
                sum += int(s[i])
        a.sort()
        for x in a:
            print(x, end = '')
        print(sum)

