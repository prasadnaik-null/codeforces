# 1328C - Ternary XOR
for _ in range(int(input())):
    l, n = int(input()), input()
    a, b = "1", "1"
    trig = False
    for i in range(1, l):
        if n[i] == "0":
            a += "0"
            b += "0"
        elif trig == False:
            if n[i] == "2":
                a += "1"
                b += "1"
            else:
                a += "1"
                b += "0"
                trig = True
        else:
            b += n[i]
            a += "0"
    print(a)
    print(b)