h,w=map(int, input().split())
S = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if S[i][j]=="#":
            count=0
            if h!=1:
                if i==0:
                    if S[i+1][j]=="#":
                        count+=1
                elif i==h-1:
                    if S[i-1][j]=="#":
                        count+=1
                else:
                    if S[i+1][j]=="#":
                        count+=1
                    if S[i-1][j]=="#":
                        count+=1
            if w!=1:
                if j==0:
                    if S[i][j+1]=="#":
                        count+=1
                elif j==w-1:
                    if S[i][j-1]=="#":
                        count+=1
                else:
                    if S[i][j+1]=="#":
                        count+=1
                    if S[i][j-1]=="#":
                        count+=1
            if count != 2 and count != 4:
                print("No")
                exit()
print("Yes")