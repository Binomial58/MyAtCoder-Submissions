S=input()
L=len(S)
A=[]
for k in range(1,L+1):
    for j in range(L+1-k):
        if A.count(S[j:j+k])==0:
            A.append(S[j:j+k])
        else:
            continue
print(len(A))