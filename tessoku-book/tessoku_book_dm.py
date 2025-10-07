n=int(input())
A=list(map(int, input().split()))
M=[0 for i in range(100)]
count=0
for a in A:
    M[a%100]+=1
for i in range(51):
    if (i==0 or i==50) and M[i]!=0:
        count += M[i%100]*(M[i%100]-1)//2
    else:
        count+=M[i]*M[(100-i)%100]
print(count)