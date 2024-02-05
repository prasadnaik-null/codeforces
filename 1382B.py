#1382B ~ prasadnaik-null
for _ in range(int(input())):
    n,l=int(input()),list(map(int,input().split()))
    one=l.count(1)
    if one==0:
        print("First")
    elif one==n:
        if one%2==1:
            print("First")
        else:
            print("Second")
    else:
        c=0
        for i in range(n):
            if l[i]!=1:
                break
            else:
                c+=1
        if c%2==0:
            print("First")
        else:
            print("Second")