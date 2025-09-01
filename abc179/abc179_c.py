n=int(input())
count=0
i=1
while i*i<=n:
    count+=((n-1)//i)*2
    count-=2*(i-1)
    i+=1
    count-=1
    if i*i==n:
        count+=1
print(count)