#509A - Maximum in Table
n,a=int(input()),1
for i in range(1,n):
  a=(a*2*((i*2)-1))//i
print(a)