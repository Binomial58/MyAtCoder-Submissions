n = int(input())
C = list(input())
l = 0
r = n - 1
count = 0
while l < r:
    if C[l] == "W" and C[r] == "R":
        C[l] = "R"
        C[r] = "W"
        count += 1
    else:
        if C[l] == "R":
            l += 1
        if C[r] == "W":
            r -= 1
print(count)