#131A - cAPS lOCK
x=input()
if len(x)==1:
  if x.isupper():
    print(x.lower())
  else:
    print(x.upper())
else:
  if x[1:].isupper():
    if x[0].isupper():
      print(x.lower())
    else:
      print(x[0].upper()+x[1:].lower())
  else:
    print(x)