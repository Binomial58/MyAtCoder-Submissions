N=int(input())
A=set()
B=set()
for i in range(N):
    S=input()
    if S[0]=="!":
        B.add(S[1:])
    else:
        A.add(S)
if len(A&B)==0:
    print("satisfiable")
else:
    print(list(A&B)[0])