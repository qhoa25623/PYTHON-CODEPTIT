if __name__ == "__main__":
    t = int(input())
    while t != 0:
        s = input()
        for i in range(len(s)):
            if s[i].isdigit():
                for j in range(int(s[i]) - 1):
                    print(s[i - 1], end = '')
            else:
                print(s[i], end =)