n,k=map(int, input().split())
A=[]
B=[]
for i in range(n):
    a,b=map(int, input().split())
    A.append(a)
    B.append(b)
countm=0
for i in range(1,101):
    for j in range(1,101):
        count=0
        for t in range(n):
            if i<=A[t]<=i+k and j<=B[t]<=j+k:
                count+=1
        countm=max(countm,count)
print(countm)