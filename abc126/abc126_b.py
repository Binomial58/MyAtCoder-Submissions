s = input()
flagy = False
flagm = False
a = int(s[:2])
b = int(s[2:])
if 1 <= a <= 12:
    flagm = True
if 1 <= b <= 12:
    flagy = True
# print(a, b)
if flagm:
    if flagy:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if flagy:
        print("YYMM")
    else:
        print("NA")
