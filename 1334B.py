#1334B ~ prasadnaik-null
for _ in range(int(input())):
    [n,x]=list(map(int,input().split()))
    a=list(map(int,input().split()))
    g,l,e=[],[],0
    for i in a:
        if i>x:
            g.append(i)
        elif i<x:
            l.append(i)
        else:
            e+=1
    gl,ll=len(g),len(l)
    if ll==0:
        print(e+gl)
    elif gl==0:
        print(e)
    else:
        gn,ln=0,0
        l=sorted(l)[::-1]
        p=False
        for j in g:
            gn+=j-x
        for k in range(ll):
            ln+=x-l[k]
            if ln>gn:
                print(gl+e+k)
                p=True
                break
        if p==False:
            print(e+gl+ll)