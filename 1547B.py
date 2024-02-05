# 1547B - Alphabetical Strings
def yea(s, n):
    try:
        m = s.index(chr(n+97))
        if len(s) == 3:
            return "YES"
        else:
            if s[m-1] == chr(n+98) or s[m+1] == chr(n+98):
                s = s[:m]+s[m+1:]
                return yea(s, n+1)
            else:
                return "NO"
    except:
        return "NO"


for _ in range(int(input())):
    c = "0"+input()+"0"
    print(yea(c, 0))