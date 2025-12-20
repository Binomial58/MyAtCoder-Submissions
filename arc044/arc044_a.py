n = int(input())
i = 2
flag = True
while i * i <= n:
    if n % i == 0:
        flag = False
    i += 1
if n == 1:
    print("Not Prime")
elif flag:
    print("Prime")
else:
    if n % 2 != 0 and n % 5 != 0 and n % 3 != 0:
        print("Prime")
    else:
        print("Not Prime")
