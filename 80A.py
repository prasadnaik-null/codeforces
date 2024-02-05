#80A - Panoramix's Prediction
import re
def isP(n):
  for i in range(2,int((n**0.5)*2)):
    if n%i==0:
      return False
  return True
[a,b]=[int(i) for i in re.split(" ",input())]
i=a
if isP(a) and isP(b):
  while True:
    i+=1
    if isP(i):
      if i==b:
        print("YES")
      else:
        print("NO")
      break
    elif i>=b:
      print("NO")
      break
else:
  print("NO")