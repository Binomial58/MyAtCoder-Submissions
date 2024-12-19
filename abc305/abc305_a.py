N=int(input())
A=[5*i for i in range(21)]
B=min([abs(a-N) for a in A ])
if (N+B)%5!=0:
    print(N-B)
else:
    print(N+B)