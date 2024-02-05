# 1480A - Yet Another String Game
for _ in range(int(input())):
    x, a = input(), ""
    for i in range(len(x)):
        if i % 2 == 0:
            if x[i] != "a":
                a += "a"
            else:
                a += "b"
        else:
            if x[i] != "z":
                a += "z"
            else:
                a += "y"
    print(a)