A,B,C,D=map(int, input().split())
X={i for i in range(A,B+1)}
Y={i for i in range(C,D+1)}
print(max(len(X&Y)-1,0))