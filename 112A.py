#85A - Petya and Strings
x=input().lower()
y=input().lower()
n=False
for i in range(len(x)):
  if x[i]>y[i]:
    print(1)
    n=True
    break
  if x[i]<y[i]:
    print(-1)
    n=True
    break
if n==False:
  print(0)