#703A - Mishka and Game
import re
M,C=0,0
for i in range(int(input())):
  [m,c]=[int(i) for i in re.split(" ",input())]
  if m>c:
    M+=1
  elif c>m:
    C+=1
if M>C:
  print("Mishka")
elif C>M:
  print("Chris")
else:
  print("Friendship is magic!^^")