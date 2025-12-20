# 最大の同じ数が連続している部分の長さを返す関数
def Count_A(A):
    count = 0
    now = 1
    for i in range(1, len(A)):
        if A[i - 1] == A[i]:
            now += 1
        else:
            count = max(now, count)
            now = 1
    count = max(now, count)
    return count


n = int(input())
H = list(map(int, input().split()))
maxlen = 1
for k in range(1, len(H)):
    i = 0
    while i != k:
        A = []
        j = 0
        while i + k * j <= len(H) - 1:
            A.append(H[i + k * j])
            j += 1
        # print(A)
        maxlen = max(maxlen, Count_A(A))
        i += 1
print(maxlen)
