N=int(input())
A=set(list(map(int, input().split())))
for _ in range(N-2):
    C=set(list(map(int, input().split())))
    A=A&C
if len(A)==1:
    print("Yes")
else:
    print("No")