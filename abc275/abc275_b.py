A,B,C,D,E,F=map(int, input().split())
N=998244353
print(((A%N*B%N*C%N)-(D%N*E%N*F%N))%N)