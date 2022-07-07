def palStr(s:str,l,r):
    if l>=r:
        return True
    if s[l]!=s[r-1]:
        return False
    return palStr(s,l+1,r-1)

# Driver code
s="abba"
l=0
r=len(s)
print(palStr(s,l,r))