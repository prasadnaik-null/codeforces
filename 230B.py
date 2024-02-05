#230B - T-prime
n=int(input())
mylist=list(map(int,input().split()))
def isPrime(n):
    if n==1 or n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
for i in mylist:
    if i**0.5%1==0 and isPrime(int(i**0.5)):
        print('YES')
    elif i==4:
        print('YES')
    else:
        print('NO')