s = input()
count = 0
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i < j < k:
                if s[i] == "A" and s[j] == "B" and s[k] == "C":
                    if i + k == 2 * j:
                        count += 1
print(count)
