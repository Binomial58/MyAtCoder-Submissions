S=input()
T=""
countW=0
R=False
if S.count("WA")==0:
    print(S)
    exit()
for i in range(len(S)):
    if R and S[i]=="A":
        T+="A"
        for k in range(countW):
            T+="C"
        countW=0
        R=False
    elif S[i]!="W":
        for k in range(countW):
            T+="W"
        T+=S[i]
        R=False
        countW=0
    elif S[i]=="W":
        countW+=1
        R=True
for k in range(countW):
    T+="W"
print(T)