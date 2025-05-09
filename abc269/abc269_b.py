S=[]
for _ in range(10):
    s=input()
    S.append(s)
for i in range(10):
    if "#"in S[i]:
        A=i+1
        break
for i in range(9,-1,-1):
    if "#"in S[i]:
        B=i+1
        break
for i in range(10):
    if S[A-1][i]=="#":
        C=i+1
        break
for i in range(9,-1,-1):
    if S[A-1][i]=="#":
        D=i+1
        break
print(A,B)
print(C,D)