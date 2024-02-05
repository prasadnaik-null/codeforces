#1579A - Casimir's String Solitaire
for i in range(int(input())):
  x=input()
  if x.count('A')+x.count('C')==x.count('B'):
    print("YES")
  else:
    print("NO")