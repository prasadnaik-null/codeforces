# 1481A - Space Navigation
for _ in range(int(input())):
    [x, y], s = list(map(int, input().split())), input()
    u, d, r, l = s.count("U"), s.count("D"), s.count("R"), s.count("L")
    if ((x > 0 and r >= x) or (x <= 0 and -l <= x)) and ((y > 0 and u >= y) or (y <= 0 and -d <= y)):
        print("YES")
    else:
        print("NO")