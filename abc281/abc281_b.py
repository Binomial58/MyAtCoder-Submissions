S=input()
b=""
if len(S)==1 or len(S)==2:
    print("No")
    exit()
#文字が数字かどうか判断
if S[0].isdigit() or S[-1].isdigit():
    print("No")
    exit()
for i in range(1,len(S)-1):
    #文字が英字か判断
    if S[i].isalpha():
        print("No")
        exit()
for i in range(1,len(S)-1):
   b+=S[i]
b=int(b)
if  b<100000 or b>999999 or S[1]=="0":
    print("No")
    exit()
print("Yes")