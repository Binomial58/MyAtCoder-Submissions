n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
# A<Bを実現できるbの集合
canB = []
canC = []
j = 0
for i in range(n):
    if B[i] > A[j]:
        canB.append(B[i])
        j += 1
k = 0
for i in range(n):
    if k == len(canB):
        break
    if C[i] > canB[k]:
        canC.append(C[i])
        k += 1
print(len(canC))
