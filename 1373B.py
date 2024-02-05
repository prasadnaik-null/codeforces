#1373B - 01 Game
for i in range(int(input())):
  x=input()
  print("DA" if min(x.count("0"),x.count("1"))%2==1 else "NET")