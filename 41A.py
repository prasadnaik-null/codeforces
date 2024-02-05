#40A - Translation
be=input()
bi=input()
w=str()
for i in range(len(be)):
  w+=be[len(be)-1-i]
if w==bi:
  print("YES")
else:
  print("NO")