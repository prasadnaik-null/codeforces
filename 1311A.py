#1311A - Add Odd or Subtract Even
import re
for i in range(int(input())):
  [a,b]=[int(i) for i in re.split(" ",input())]
  if b>a:
    if (b-a)%2==1:
      print(1)
    else: 
      print(2)
  elif a>b:
    if (a-b)%2==0:
      print(1)
    else:
      print(2)
  else:
    print(0)