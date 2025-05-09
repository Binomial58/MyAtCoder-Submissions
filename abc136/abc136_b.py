N=int(input())
S=0
for i in range(1,N+1):
    if i<10 or 99<i<1000 or 9999<i<100000:
        S+=1
print(S)