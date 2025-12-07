import itertools

s = input()
# 出てくる可能性がある数字の管理
S = []
# 丸であるものの管理
C = []
# 集合による管理
Count = set()
for i in range(10):
    if s[i] == "o":
        S.append(i)
        C.append(i)
    elif s[i] == "?":
        S.append(i)
count = 0
for v in itertools.combinations_with_replacement(S, 4):
    flag = True
    for c in C:
        if c not in v:
            flag = False
            break
    if flag:
        Count.add(v)
for c in Count:
    Sc = set()
    for u in itertools.permutations(c):
        Sc.add(u)
    count += len(Sc)
print(count)
