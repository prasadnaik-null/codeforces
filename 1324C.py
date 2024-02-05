#1324C
for _ in range(int(input())):
	x=input()
	c=0
	m=0
	for i in x:
		if i=="L":
			c+=1
		else:
			if c>m:
				m=c
			c=0
	if c>m:
		m=c
	print(m+1)