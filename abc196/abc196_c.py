n=input()
l=len(n)
if l==1:
    print(0)
    exit()
if l%2==0:
    a=int(n[:l//2])
    c=0
    for i in range(1,a+1):
        if int(str(i)+str(i))<=int(n):
            c+=1
    print(c)
else:
    print(9*int("1"*(l//2)))