A,B=map(int, input().split())
C=0
for i in range(A,B+1):
    S=str(i)
    if S==S[::-1]:
        C+=1
print(C)