s=input()
T=""
for i in s:
    if i == ",":
        T+=" "
    else:
        T+=i
print(T)