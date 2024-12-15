S=input()
N=len(S)
if S[0]=="<" and S[N-1]==">" and all([S[i]=="="for i in range(1,N-1)]):
    print("Yes")
else:
    print("No")