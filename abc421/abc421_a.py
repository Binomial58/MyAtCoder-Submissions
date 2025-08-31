n=int(input())
S=[]
for i in range(n):
    s=input()
    S.append(s)
x,y=map(str, input().split())
if S[int(x)-1]==y:
    print("Yes")
else:
    print("No")