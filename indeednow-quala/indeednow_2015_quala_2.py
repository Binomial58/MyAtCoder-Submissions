n=int(input())
R=[]
S=list("indeednow")
S.sort()
for i in range(n):
    s=input()
    s=list(s)
    s.sort()
    if s==S:
        R.append("YES")
    else:
        R.append("NO")
for r in R:
    print(r)