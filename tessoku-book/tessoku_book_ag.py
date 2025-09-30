n=int(input())
A=list(map(int, input().split()))
now=0
for a in A:
    now^=a
if now==0:
    print("Second")
else:
    print("First")