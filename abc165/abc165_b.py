X=int(input())
N=100
C=0
while N<X:
    N=N+N//100
    C+=1
print(C)
#浮動小数点の誤差を避けるためになるべく小数は使わない