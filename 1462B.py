# 1462B - Last Year's Substring
for _ in range(int(input())):
    x, y = input(), input()
    z = y[::-1]
    if (y[:2] == "20" and z[:2] == "02") or (y[:1] == "2" and z[:3] == "020") or (y[:3] == "202" and z[:1] == "0") or y[:4] == "2020" or z[:4] == "0202":
        print("YES")
    else:
        print("NO")