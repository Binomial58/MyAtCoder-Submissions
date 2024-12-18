N=int(input())
A=[j for j in range(1,10) if N%j==0]
B=""
for i in range(N+1):
    k=0
    for j in A:
        if i%(N/j)==0 and k==0:
            #jを文字列に加えるためにstrに変換
            B+=str(j)
            k+=1
    if k==0:
        B+="-"
print(B)