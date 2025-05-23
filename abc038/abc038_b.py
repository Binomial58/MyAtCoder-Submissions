A=list(map(int, input().split()))
B=list(map(int, input().split()))
if A[0]==B[0] or A[0]==B[1] or A[1]==B[0] or A[1]==B[1]:
    print("YES")
else:
    print("NO")