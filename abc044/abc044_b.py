w=input()
count={}
set=set()
for i in w:
    if i not in count:
        count[i]=1
        set.add(i)
    else:
        count[i]+=1
for c in set:
    if count[c]%2==1:
        print("No")
        exit()
print("Yes")