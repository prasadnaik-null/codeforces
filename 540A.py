#540A - Combination Lock
x,y,z,c=int(input()),input(),input(),0
for i in range(x):
  a=abs(int(y[i])-int(z[i]))
  c+=min(a,10-a)
print(c)