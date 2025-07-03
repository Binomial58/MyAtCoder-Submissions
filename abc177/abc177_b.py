S=input()
T=input()
m=10**10
for i in range(len(S)-len(T)+1):
    s=0
    for j in range(len(T)):
        if T[j]!=S[i+j]:
            s+=1
    m=min(m,s)
print(m)