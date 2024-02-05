# 550A - Two Substrings
import re
x = input()
ab = len(re.findall(r'(?=AB)', x))
ba = len(re.findall(r'(?=BA)', x))
aba = len(re.findall(r'(?=ABA)', x))
bab = len(re.findall(r'(?=BAB)', x))
y = aba+bab
if (ab > 0 and ba > 0 and (ab > y or ba > y)) or len(re.findall("BABAB", x)) > 0 or len(re.findall("ABABA", x)) > 0:
    print("YES")
else:
    print("NO")