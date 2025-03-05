A,B=map(int, input().split())
C=0
for _ in range(2):
    if A>B:
        C+=A
        A-=1
    else:
        C+=B
        B-=1
print(C)