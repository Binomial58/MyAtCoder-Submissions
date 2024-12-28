K=int(input())
d=0
S=input()
T=input()
if abs(len(S)-len(T))>1 or len(set(T)-set(S))>1:
    print("No")
    exit()
if abs(len(S)-len(T))==1:
    d+=1
for i in range(min(len(S),len(T))):
    if S[i]!=T[i] :
        if d==0 and S[i+1:]!=T[i+1:]:
            print("No")
            exit()
        elif i!=min(len(S),len(T))-1 and S[i]!=T[i+1] and S[i+1]!=T[i]:
            d+=1
    if d>1:
        print("No")
        exit()
if min(len(S),len(T))==1 and len(set(S))==1 and len(set(T))==1 and S[0]!=T[0] and max(len(S),len(T))!=1:
    print("No")
    exit()
print("Yes")