N,M=map(int, input().split())
S=input()
T=input()
#Tの中にSが含まれない場合は終了
if T.count(S)==0:
    print(3)
    exit()
#接頭辞の先頭のインデックスの候補
X=T.index(S)
#接尾語の先頭のインデックスの候補
Y=T.rindex(S)
if X==0:
    if Y==M-N:
        print(0)
    else:
        print(1)
else:
    if Y==M-N:
        print(2)
    else:
        print(3)