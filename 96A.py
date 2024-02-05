#77A - Football
x=input()
c=x[0]
l=0
for i in range(len(x)):
  if x[i]==c:
    l+=1
  else:
    c=x[i]
    l=1
  if l==7:
    print("YES")
    break
if l<7:
  print("NO")