#54A - Chat room
import re
s=re.findall("h\w*e\w*l\w*l\w*o",input())
try:
  if s[0]!=None:
    print("YES")
except:
  print("NO")