S=input()
#S[3:]でインデックス3以降の文字を抽出
D=int(S[3:])
if 1<=D<=349 and D!=316:
    print("Yes")
else:
    print("No")