N=int(input())
if N%2==0:
    print("-"*(N//2-1)+"=="+"-"*(N//2-1))
else:
    print("-"*((N-1)//2)+"="+"-"*((N-1)//2))