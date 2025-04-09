M,D=map(int, input().split())
S=0
if D<22:
    print(0)
    exit()
for d in range(22,D+1):
    if str(d)[1]=="0" or str(d)[1]=="1":
        continue    
    if int(str(d)[1])*int(str(d)[0])<=M:
        S+=1
print(S)