# 1354B - Ternary String
import re
for _ in range(int(input())):
    x = input()
    match = [re.finditer(r"(?=(12+3))", x), re.finditer(r"(?=(13+2))", x), re.finditer(r"(?=(21+3))", x),
             re.finditer(r"(?=(23+1))", x), re.finditer(r"(?=(32+1))", x), re.finditer(r"(?=(31+2))", x)]
    matchl = []
    for i in match:
        matchl += [len(i.group(1)) for i in i]
    try:
        print(min(matchl))
    except:
        print(0)