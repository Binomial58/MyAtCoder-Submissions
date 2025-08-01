S=list(input())
T=list(input())
R=[]
u=0
d=0
for i in range(len(S)):
    if ord(S[i])>ord(T[i]):
        u+=1
    elif ord(S[i])<ord(T[i]):
        d+=1
for i in range(u):
    for j in range(len(S)):
        if ord(S[j])>ord(T[j]):
            S[j]=T[j]
            R.append("".join(S))
            break
for i in range(d):
    for j in range(len(S)-1,-1,-1):
        if ord(S[j])<ord(T[j]):
            S[j]=T[j]
            R.append("".join(S))
            break
print(u+d)
for r in R:
    print(r)