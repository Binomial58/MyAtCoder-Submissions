S = input()
a = 0
count = len(S)
for i in range(len(S) - 1, -1, -1):
    count += (int(S[i]) + 10 - a) % 10
    a += (int(S[i]) + 10 - a) % 10
print(count)
