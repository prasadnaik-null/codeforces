# 1676A - Lucky?
for _ in range(int(input())):
    x = input()
    if int(x[0])+int(x[1])+int(x[2]) == int(x[3])+int(x[4])+int(x[5]):
        print("YES")
    else:
        print("NO")