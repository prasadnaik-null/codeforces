# 1555A - PizzaForces
for _ in range(int(input())):
    x = int(input())
    y = x % 6
    if x < 6:
        print(15)
    elif y == 1 or y == 2:
        print((x//6)*15+5)
    elif y == 3 or y == 4:
        print((x//6)*15+10)
    elif y == 5:
        print((x//6)*15+15)
    else:
        print((x//6)*15)