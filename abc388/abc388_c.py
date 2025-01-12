#二分探索を行うためのbisectライブラリ
import bisect
N=int(input())
A=list(map(int, input().split()))
count=0
for a in A:
    #二分探索でa//2がAにおいてどのインデックスになるかを計算する．
    count+=bisect.bisect(A,a//2)
print(count)