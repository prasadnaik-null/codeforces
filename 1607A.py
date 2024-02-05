#1607A - Linear Keyboard
for i in range(int(input())):
  a,b,m=input(),input(),0
  for i in range(len(b)-1):
    m+=abs(a.index(b[i])-a.index(b[i+1]))
  print(m)