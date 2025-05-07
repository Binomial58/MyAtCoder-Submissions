A=[111*i for i in range(1,10)]
N=int(input())
if N<=111:
    print(111)
    exit()
for j in range(1,10):
    if A[j-1]<N<=A[j]:
        print(A[j])
        exit()
print(A[-1])