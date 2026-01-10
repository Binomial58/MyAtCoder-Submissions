s = input()
R = []
for t in s:
    if t.isupper():
        R.append(t)
print("".join(R))
