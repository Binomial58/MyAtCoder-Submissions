A,B=map(int, input().split())
a=A/0.08
b=(A+1)/0.08
c=B/0.1
d=(B+1)/0.1
m=-1
for i in range(1,int(1000//0.08)):
    if a<=i<b and c<=i<d:
        m=i
        print(m)
        exit()
print(m)
