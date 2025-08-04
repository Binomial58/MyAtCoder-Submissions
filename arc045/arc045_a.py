S=list(map(str, input().split()))
T=[]
for s in S:
    if s=="Left":
        T.append("<")
    elif s=="Right":
        T.append(">")
    else:
        T.append("A")
print(*T)