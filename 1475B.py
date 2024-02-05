#475B - New Year's Number
for i in range(int(input())):
  x=int(input())
  if x//2020>=x%2020:
    print("YES")
  else:
    print("NO")