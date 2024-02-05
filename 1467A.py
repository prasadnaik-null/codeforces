# 1467A - Wizard of Orz
for _ in range(int(input())):
    x = int(input())
    if x == 1:
        print(9)
    elif x == 2:
        print(98)
    else:
        print("989"+"0123456789"*((x-3)//10)+"0123456789"[:(x-3) % 10])