N=int(input())
A=map(int, input().split())
S=sum(A)
if S%2==1:
    print("NO")
else:
    print("YES")