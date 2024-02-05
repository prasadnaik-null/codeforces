#133A - HQ9+
s=input()
k=False
for i in range(len(s)):
  if s[i]=="H" or s[i]=="Q" or s[i]=="9":
    print("YES")
    k=True
    break
if k==False:
  print("NO")