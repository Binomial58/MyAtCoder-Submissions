def Dsum(n):
    now = 0
    for i in n:
        now += int(i)
    return now


n = input()
if n[0] == "1":
    print(max(Dsum(n), Dsum(str(9) * (len(n) - 1))))
else:
    print(max(Dsum(n), Dsum(str(int(n[0]) - 1) + str(9) * (len(n) - 1))))
