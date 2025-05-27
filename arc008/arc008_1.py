N=int(input())
if N%10>6 or N%10==0:
    if N%10==0:
        print(100*(N//10))
    else:
        print(100*(N//10+1))
else:
    print(100*(N//10)+15*(N%10))