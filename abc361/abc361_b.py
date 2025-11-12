A = list(map(int, input().split()))
B = list(map(int, input().split()))
if ((A[3] - B[0]) * (A[4] - B[1]) * (A[5] - B[2]) > 0) and (
    (B[3] - A[0]) * (B[4] - A[1]) * (B[5] - A[2]) > 0
):
    print("Yes")
else:
    print("No")
