import math
N=int(input())
for i in range(1,50001):
    if math.floor(i*1.08)==N:
        print(i)
        exit()
print(":(")