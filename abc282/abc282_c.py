N=int(input())
S=input()
A=0
T=""
for i in range(N):
    if S[i]=="\"" and A==0:
        A=1
        T+="\""
        continue
    if S[i]=="\"" and A==1:
        A=0
        T+="\""
        continue
    if S[i]=="," and A==0:
        T+="."
        continue
    T+=S[i]
print(T)