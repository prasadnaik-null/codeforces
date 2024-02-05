#228A - Is your horseshoe on the other hoof?
import re
x=[int(i) for i in re.split(" ",input())]
l,c=[],0
for i in range(4):
  if x[i] in l:
    c+=1
  else:
    l.append(x[i])
print(c)