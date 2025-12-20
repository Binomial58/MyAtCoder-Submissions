def cross(A, B):
    d = A[0] * B[1] - A[1] * B[0]
    if d > 0:
        return 1
    else:
        return -1


X = []
for i in range(4):
    X.append(list(map(int, input().split())))
A = [X[2][0] - X[0][0], X[2][1] - X[0][1]]
B = [X[1][0] - X[0][0], X[1][1] - X[0][1]]
C = [X[3][0] - X[0][0], X[3][1] - X[0][1]]
if cross(A, B) == cross(A, C):
    print("No")
    exit()
A = [X[3][0] - X[1][0], X[3][1] - X[1][1]]
B = [X[0][0] - X[1][0], X[0][1] - X[1][1]]
C = [X[2][0] - X[1][0], X[2][1] - X[1][1]]
if cross(A, B) == cross(A, C):
    print("No")
else:
    print("Yes")
