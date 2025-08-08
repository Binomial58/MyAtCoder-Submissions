n=int(input())
h=str(n//3600)
n%=3600
m=str(n//60)
n%=60
s=str(n)
if len(h)==1:
    h="0"+str(h)
if len(m)==1:
    m="0"+str(m)
if len(s)==1:
    s="0"+str(s)
print(h+":"+m+":"+s)