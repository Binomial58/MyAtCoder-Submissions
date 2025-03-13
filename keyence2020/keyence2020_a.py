H=int(input())
W=int(input())
N=int(input())
R=max(H,W)
if N%(R)==0:
    print(N//R)
else:
    print(N//R+1)