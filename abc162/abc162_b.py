N=int(input())
S=int(0.5*N*(N+1))
a=N//3
b=N//5
c=N//15
S=S-3*(0.5*a*(a+1))-5*(0.5*b*(b+1))+15*(0.5*c*(c+1))
print(int(S))