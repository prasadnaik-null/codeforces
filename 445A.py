#445A ~ prasadnaik-null
[n,m]=list(map(int,input().split()))
for j in range(n):
    x,y=input(),""
    if j%2==0:
        for i in range(m):
            if x[i]=="-":
                y+="-"
            else:
                if i%2==0:
                    y+="B"
                else:
                    y+="W"
    else:
        for i in range(m):
            if x[i]=="-":
                y+="-"
            else:
                if i%2==0:
                    y+="W"
                else:
                    y+="B"
    print(y)