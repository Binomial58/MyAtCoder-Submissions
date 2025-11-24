import collections

At = ["a", "t", "c", "o", "d", "e", "r"]
# 元の文字列
s = input()
t = input()
# atcoderのいずれかであるもの
Sa = []
Ta = []
# atcoderのいずれかでないもの
Sna = []
Tna = []
for i in range(len(s)):
    if s[i] != "@":
        if s[i] in At:
            Sa.append(s[i])
        else:
            Sna.append(s[i])
    if t[i] != "@":
        if t[i] in At:
            Ta.append(t[i])
        else:
            Tna.append(t[i])
sa = len(s) - len(Sa) - len(Sna)
ta = len(t) - len(Ta) - len(Tna)
Sa = collections.Counter(Sa)
Ta = collections.Counter(Ta)
Sna = collections.Counter(Sna)
Tna = collections.Counter(Tna)
if Sna != Tna:
    print("No")
else:
    for e in At:
        # print(Sa[e], Ta[e])
        # print(sa, ta)
        if Sa[e] > Ta[e]:
            ta -= Sa[e] - Ta[e]
            Ta[e] += Sa[e] - Ta[e]
        elif Ta[e] > Sa[e]:
            sa -= Ta[e] - Sa[e]
            Sa[e] += Ta[e] - Sa[e]
    if sa >= 0 and ta >= 0 and Sa == Ta:
        print("Yes")
    else:
        print("No")
# print(Sa)
# print(Sna)
# print(Ta)
# print(Tna)
# print(sa)
# print(ta)
