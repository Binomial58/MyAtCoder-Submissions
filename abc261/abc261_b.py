N=int(input())
A=[]
for _ in range(N):
    a=input()
    A.append(a)
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        elif A[i][j]==A[j][i]:
                if A[i][j]!="D":
                    print("incorrect")
                    exit()
        elif A[i][j]=="L" and A[j][i]!="W":
             print("incorrect")
             exit()
        elif A[i][j]=="W" and A[j][i]!="L":
             print("incorrect")
             exit()
print("correct")