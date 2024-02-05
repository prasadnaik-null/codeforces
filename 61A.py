#61A - Ultra-Fast Mathematician
n1=input()
n2=input()
a=str()
for i in range(len(n1)):
  if n1[i]==n2[i]:
    a=a+"0"
  else:
    a=a+"1"
print(a)