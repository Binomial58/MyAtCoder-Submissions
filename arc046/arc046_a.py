N=int(input())
a=N//9+1
b=N%9
if b==0:
    b=9
    a-=1
print(str(b)*a)