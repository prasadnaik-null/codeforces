# 1611A - Make Even
for _ in range(int(input())):
    s = input()
    if "2" not in s and "4" not in s and "6" not in s and "8" not in s:
        print(-1)
    elif int(s[-1]) % 2 == 0:
        print(0)
    elif int(s[0]) % 2 == 0:
        print(1)
    else:
        print(2)