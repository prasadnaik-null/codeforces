#1374C - Move Brackets
for i in range(int(input())):
  n,x,m=int(input()),input(),0
  for j in x:
    if j=="(":
      m+=1
    else:
      if m>0:
        m-=1
  print(m)