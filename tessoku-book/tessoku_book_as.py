n,c=map(str, input().split())
s=input()
count=0
for a in s:
    if a=="B":
        count+=1
    elif a=="R":
        count+=2
if c=="W":
    f=0
elif c=="B":
    f=1
else:
    f=2
if f==count%3:
    print("Yes")
else:
    print("No")