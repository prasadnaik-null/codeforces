# 1469A - Regular Bracket Sequence
for _ in range(int(input())):
    x = list(input().strip(""))
    if len(x) % 2 == 1:
        print("NO")
    else:
        l = len(x)//2
        a, b, c, k = l-x.count("("), l-x.count(")"), 0, 0
        for i in range(l*2):
            if x[i] == "?":
                if a > 0:
                    x[i] = "("
                    a -= 1
                elif b > 0:
                    x[i] = ")"
                    b -= 1
            if a == 0 and b == 0:
                break
        # print(x)
        for i in x:
            if i == "(":
                k += 1
            else:
                k -= 1
            if k < 0:
                print("NO")
                break
            # print(x)
        if k == 0:
            print("YES")