a,b=map(int, input().split())
S=0
for i in range(b-a):
    S+=i
print(S-a)