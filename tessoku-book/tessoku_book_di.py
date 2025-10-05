n,k=map(int, input().split())
sum=0
s=input()
for i in s:
    sum+=int(i)
if (abs(k-sum))%2==0:
    print("Yes")
else:
    print("No")