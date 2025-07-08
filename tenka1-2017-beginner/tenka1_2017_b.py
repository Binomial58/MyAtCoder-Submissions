N=int(input())
A=[]
B=[]
for i in range(N):
    a,b=map(int, input().split())
    A.append(a)
    B.append(b)
A, B = zip(*sorted(zip(A, B)))
print(A[-1]+B[-1])