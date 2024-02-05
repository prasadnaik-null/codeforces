#32B - Borze
n,y,i=input(),str(),0
while i<len(n):
  if n[i]=="-":
    if n[i+1]==".":
      y+="1"
    else:
      y+="2"
    i+=2
  else:
    y+="0"
    i+=1
print(y)