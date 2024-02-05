#705A - Hulk
n,s=int(input()),str()
for i in range(1,n+1):
  if i!=n:
    if i%2==1:
      s+="I hate that "
    else:
      s+="I love that "
  else:
    if i%2==1:
      s+="I hate it"
    else:
      s+="I love it"
print(s)