# 1644A - Doors and Keys
import re
for _ in range(int(input())):
    s = input()
    if re.search("r.*R", s) == None or re.search("b.*B", s) == None or re.search("g.*G", s) == None:
        print("NO")
    else:
        print("YES")