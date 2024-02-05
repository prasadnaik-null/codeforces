# 1517A - Sum of 2050
def a(i):
    if i == 0:
        return 0
    else:
        return i % 10 + a(i//10)


for _ in range(int(input())):
    s = int(input())
    if s % 2050 == 0:
        print(a(s//2050))
    else:
        print(-1)