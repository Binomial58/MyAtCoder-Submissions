N=int(input())
a=N//4
b=N%4
print(2*(4*a+b))
if b==0:
    print(str(4)*a)
else:
    print(str(b)+str(4)*a)