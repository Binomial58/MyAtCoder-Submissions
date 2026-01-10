A = list(map(int, input().split()))
count = 0
R = []
for i in range(5):
    if A[i] != i + 1:
        count += 1
        R.append(i)
if count != 2:
    print("No")
else:
    if R[0] + 1 == R[1]:
        print("Yes")
    else:
        print("No")
