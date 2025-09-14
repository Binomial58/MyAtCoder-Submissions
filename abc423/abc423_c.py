n,r=map(int, input().split())
L=list(map(int, input().split()))
Left=L[:r][::-1]
Right=L[r:]
count=0
for i in range(len(Left)):
    if Left[len(Left)-i-1]==1:
        count+=1
    else:
        break
Left=Left[:len(Left)-count]
count=0
for i in range(len(Right)):
    if Right[len(Right)-i-1]==1:
        count+=1
    else:
        break
Right=Right[:len(Right)-count]
print(sum(Right)+sum(Left)+len(Right)+len(Left))