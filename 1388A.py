# 1388A - Captain Flint and Crew Recruitment
for _ in range(int(input())):
    x = int(input())
    if x <= 30:
        print("NO")
    else:
        print("YES")
        if x == 40:
            print("6 14 15 5")
        elif x == 44:
            print("6 10 15 13")
        elif x==36:
            print("5 6 10 15")
        else:
            print("6 10 14", x-30)