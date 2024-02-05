for _ in range(int(input())):
	n = int(input())
	l = list(map(int,input().split()))
	s = [0]*n
	for i in l:
		s[i-1] += 1
	if 1 in s:
		print(l.index(s.index(1)+1)+1)
	else:
		print(-1)