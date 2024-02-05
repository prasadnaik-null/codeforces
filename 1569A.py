# 1569 - Balanced Substring
for _ in range(int(input())):
    n, s = int(input()), input()
    if s.count("b") == 0 or s.count("a") == 0:
        print("-1 -1")
    else:
        for i in range(n):
            if s[i:i+2] == "ba" or s[i:i+2] == "ab":
                print(i+1, i+2)
                break