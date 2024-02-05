#1454A - Special Permutation
for i in range(int(input())):
  print(*([int(i) for i in range(2,int(input())+1)]+[1]))