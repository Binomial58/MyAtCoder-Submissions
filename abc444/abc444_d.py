n = int(input())
A = list(map(int, input().split()))
Ans = [0 for i in range(max(A) + 100)]
for a in A:
    Ans[0] += 1
    Ans[a] -= 1
for i in range(1, len(Ans)):
    Ans[i] += Ans[i - 1]
for i in range(len(Ans) - 1):
    if Ans[i] >= 10:
        Ans[i + 1] += Ans[i] // 10
        Ans[i] %= 10
# print(Ans)

while Ans[-1] == 0:
    Ans.pop()
R = ["" for i in range(len(Ans[::-1]))]
T = Ans[::-1]
# print(T)
for i in range(len(Ans[::-1])):
    R[i] = str(T[i])
print("".join(R))
