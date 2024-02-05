#1355A ~ prasadnaik-null
def ans(a): # -> int
    s=str(a)
    min,max=9,0
    if "0" not in s:
        for i in range(len(s)):
            if max!=9:
                if int(s[i])>max:
                    max=int(s[i])
            if min!=1:
                if int(s[i])<min:
                    min=int(s[i])
        return [a+(min*max),1]
    else:
        return [a,0]

for _ in range(int(input())):
    [a,k]=list(map(int,input().split()))
    for _ in range(k-1):
        [a,c]=ans(a)
        if c==0:
            break
    print(a)