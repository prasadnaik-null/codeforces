# 1451A - Subtract or Divide
for _ in range(int(input())):
    x = int(input())
    if x > 3:
        if x % 2 == 0:
            print(2)
        else:
            print(3)
    else:
        if x == 1:
            print(0)
        elif x == 2:
            print(1)
        else:
            print(2)