N=int(input())
S=input()
T=[]
i=0
while i<N:
    if S[i]=="C":
        T.append("C")
        i+=1
    else:
        p=0
        j=i
        while j<N and S[j]!="C":
            if S[j]=="A":
                p+=2
            else:
                p+=1
            j+=1
        T.append("A"*(p//2))
        T.append("B"*(p%2))
        i+=j-i
print("".join(T))
#愚直に計算するのではなく規則性を見つけて実装する．