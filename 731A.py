#731A - Night at the Museum
x,a="a"+input(),0
c=ord(x[0])
for i in range(len(x)-1):
  b,c=c,ord(x[i+1])
  z=abs(b-c)
  a+=min(z,26-z)
print(a)