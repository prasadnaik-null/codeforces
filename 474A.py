#474A - Keyboard
x,s,z,y=input(),input(),"qwertyuiopasdfghjkl;zxcvbnm,./",str()
a=(-1 if x=="R" else 1)
for i in s:
  y+=z[z.index(i)+a]
print(y)