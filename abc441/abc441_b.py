n,m=map(int, input().split())
s=input()
t=input()
q=int(input())
R=[]
for i in range(q):
    w=input()
    flagt=True
    flaga=True
    for wa in w:
        if wa not in s:
            flagt=False
        if wa not in t:
            flaga=False
    if flagt:
        if flaga:
            R.append("Unknown")
        else:
            R.append("Takahashi")
    else:
        if flaga:
            R.append("Aoki")
        else:
            R.append("Unknown")
for r in R:
    print(r)