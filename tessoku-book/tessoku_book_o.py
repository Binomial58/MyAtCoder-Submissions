import bisect
import copy
n=int(input())
A=list(map(int, input().split()))
C=copy.deepcopy(list(set(A)))
C.sort()
B=[]
for a in A:
    B.append(bisect.bisect_left(C,a)+1)
print(*B)