#742A - Arpas hard exam and Mehrdads naive cheat
n,m=int(input()),{1:8,2:4,3:2,0:6}
print(1 if n==0 else m[n%4])