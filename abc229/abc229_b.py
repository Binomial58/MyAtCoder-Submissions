A,B=map(str, input().split())
if len(A)<len(B):
    A="0"*(len(B)-len(A))+A
else:
    B="0"*(len(A)-len(B))+B
for i in range(len(A)):
    if int(A[i])+int(B[i])>=10:
        print("Hard")
        exit()
print("Easy")