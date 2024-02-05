#55A - Word
s=input()
l,u=0,0
for i in range(len(s)):
  if s[i].islower():
    l+=1
  else:
    u+=1
if l>=u:
  print(s.lower())
else:
  print(s.upper())