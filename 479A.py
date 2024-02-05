#479A - Expression
x1=int(input())
x2=int(input())
x3=int(input())
if x1>x3:
  if x3+x2>x3*x2:
    if x1+(x3+x2)>x1*(x3+x2):
      print(x1+(x3+x2))
    else:
      print(x1*(x3+x2))
  else:
    if x1+(x3*x2)>x1*(x3*x2):
      print(x1+(x3*x2))
    else:
      print(x1*(x3*x2))
else:
  if x1+x2>x1*x2:
    if x3+(x1+x2)>x3*(x1+x2):
      print(x3+(x1+x2))
    else:
      print(x3*(x1+x2))
  else:
    if x3+(x1*x2)>x3*(x1*x2):
      print(x3+(x1*x2))
    else:
      print(x3*(x1*x2))