L,R,d=map(int, input().split())
count=0
for i in range(L,R+1):
    if i%d==0:
        count+=1
print(count)