n, q = map(int, input().split())
l = 1
r = 2
count=0
for i in range(q):
    h,t=map(str, input().split())
    t=int(t)
    if h=="R":
        now=r
        c=0
        while now != t:
            now +=1
            if now ==n+1:
                now=1
            c+=1
            if now == l:
                c=0
                now=r
                while now != t:
                    now-=1
                    count+=1
                    if now ==0:
                        now=n
                break
        count+=c
        r=now
    else:
        now=l
        c=0
        while now != t:
            now+=1
            if now ==n+1:
                now=1
            c+=1
            if now == r:
                c=0
                now=l
                while now != t:
                    now-=1
                    count+=1
                    if now ==0:
                        now=n
                break
        count+=c
        l=now
print(count)
