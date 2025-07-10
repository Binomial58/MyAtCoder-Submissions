l,h=map(int, input().split())
n=int(input())
R=[]
for r in range(n):
    a=int(input())
    if a<l:
        R.append(l-a)
    elif l<=a<=h:
        R.append(0)
    else:
        R.append(-1)
for r in R:
    print(r)