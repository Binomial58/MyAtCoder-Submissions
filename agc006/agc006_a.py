n = int(input())
s = input()
t = input()
for i in range(n):
    flag = True
    for j in range(n - i):
        if s[i + j] != t[j]:
            flag = False
    if flag:
        print(n + i)
        exit()
print(2 * n)
