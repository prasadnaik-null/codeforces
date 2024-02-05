n=int(input())
p,s=[int(input())for i in range(n)],0
for i in range(n):
	c=0
	while i>=0:i=p[i]-1;c+=1
	s=max(s,c)
print(s)