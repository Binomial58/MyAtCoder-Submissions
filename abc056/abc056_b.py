W,a,b=map(int, input().split())
if b-(a+W)<0 and a-(b+W)<0:
    print(0)
else:
    print(max(b-(a+W),a-(b+W)))