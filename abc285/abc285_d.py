n = int(input())
Name = dict()
Name2 = dict()
Namedone = dict()
for i in range(n):
    s, t = map(str, input().split())
    Name[s] = t
    Name2[t] = s
    Namedone[s] = False
for na in Name:
    # print(Namedone)
    k = na
    if Namedone[na]:
        continue
    Namedone[k] = True
    # 下に探索していく
    while Name[k] in Name:
        k = Name[k]
        if Namedone[k]:
            # print(na, k)
            print("No")
            exit()
        else:
            Namedone[k] = True
    k = na
    while k in Name2:
        k = Name2[k]
        if Namedone[k]:
            print("No")
            exit()
        else:
            Namedone[k] = True
print("Yes")
