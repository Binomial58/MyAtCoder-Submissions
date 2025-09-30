n,h,w=map(int, input().split())
now=0
for i in range(n):
    a,b=map(int, input().split())
    now^=(a-1)
    now^=(b-1)
if now==0:
    print("Second")
else:
    print("First")