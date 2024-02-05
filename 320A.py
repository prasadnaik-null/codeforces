# 320A - Magic Numbers
import re
x = input()
if x.count("1")+x.count("4") < len(x) or x[0] == "4" or len(max([""]+re.findall("14+", x))) > 3:
    print("NO")
else:
    print("YES")