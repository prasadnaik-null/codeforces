#313A - Ilya and Bank Account
x=input()
print(max(int(x),int(x[:-1]),int(x[:-2]+x[-1])))