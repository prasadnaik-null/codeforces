#1567A - Domino Disaster
for i in range(int(input())):
  n,x,i,ans=int(input()),input(),0,""
  while i<n:
    a=x[i]
    try:
      b=x[i+1]
      if a=="L":
        if b=="R":
          ans+="LR"
          i+=2
        else:
          ans+="R" 
          i+=1
      elif a=="R":
        if b=="L":
          ans+="RL"
          i+=2
        else:
          ans+="L" 
          i+=1
      elif a=="U":
        if b=="D":
          ans+="UD"
          i+=2
        else:
          ans+="D" 
          i+=1
      else:
        if b=="U":
          ans+="DU"
          i+=2
        else:
          ans+="U" 
          i+=1
    except:
      if a=="L":
        ans+="R" 
      elif a=="R":
        ans+="L"
      elif a=="U":
        ans+="D"
      else:
        ans+="U"
      break
  print(ans)