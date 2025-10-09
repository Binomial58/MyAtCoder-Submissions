import math
n=int(input())
for i in range(1,math.ceil(math.log(n,5)+100)):
    a=n-5**i
    j=1
    b=5**i
    while 3**j<a:
        j+=1
    if 3**j+b==n:
        print(j,i)
        exit()
print(-1)