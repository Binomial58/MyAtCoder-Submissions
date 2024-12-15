S=input()
T=input()
A=[]
a=0
for i in range(len(T)):
    if T[i]==S[a]:
        A.append(i+1)
        a+=1
print(*A)