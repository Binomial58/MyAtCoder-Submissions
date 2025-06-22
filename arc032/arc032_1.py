n=int(input())
N=n*(n+1)//2
if N==1:
    print("BOWWOW")
    exit()
for i in range(2,N+1):
    if i*i>N:
        break
    if N%i==0:
        print("BOWWOW")
        exit()
print("WANWAN")