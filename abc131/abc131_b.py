N,L=map(int, input().split())
T=[L+i-1 for i in range(1,N+1)]
R=[abs(L+i-1) for i in range(1,N+1)]
S=sum(T)
print(S-T[R.index(min(R))])