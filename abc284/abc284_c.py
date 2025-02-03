N,M=map(int, input().split())
T=[[i] for i in range(1,N+1)]
C=0
for i in range(M):
    A,B=map(int, input().split())
    a=min(A,B)
    b=max(A,B)
    count=0
    for k in range(len(T)):
        if T[k].count(a)==1 and T[k].count(b)==0 and count==0:
            count+=1
            for j in range(len(T)):
                if T[j].count(b)==1 :
                    for o in T[j]:
                        T[k].append(o)
                    T.pop(j)
                    T.append([0])
                    C+=1
                    break
print(len(T)-C)