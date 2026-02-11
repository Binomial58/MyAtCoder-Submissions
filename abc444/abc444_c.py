n = int(input())
A = list(map(int, input().split()))
A.sort()
B = []
maxa = max(A)
for a in A:
    if a != maxa:
        B.append(a)
Ans = []
c = A[0] + A[-1]
can = True
if n % 2 == 0:
    for i in range(n // 2):
        # print(A[i], A[n - 1 - i])
        if A[i] + A[n - 1 - i] != c:
            can = False
            break
    if can:
        Ans.append(c)
can = True
if A[0] == maxa:
    Ans.append(maxa)
else:
    if (len(B)) % 2 == 0:
        for i in range(n // 2):
            # print(B[i], B[len(B) - 1 - i])
            if A[i] + A[len(B) - 1 - i] != maxa:
                can = False
                break
        if can:
            Ans.append(maxa)
# print(A)
# print(B)
Ans.sort()
print(*Ans)
