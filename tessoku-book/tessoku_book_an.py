n=int(input())
A=list(map(int, input().split()))
B=set(A)
count=0
for b in B:
    e=A.count(b)
    if e >=3:
        count+=(e*(e-1)*(e-2))//6
print(count)
