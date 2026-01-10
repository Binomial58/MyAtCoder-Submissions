from collections import Counter

n = int(input())
A = list(map(int, input().split()))
if n % 3 != 0:
    if sum(A) == 0:
        print("Yes")
    else:
        print("No")
else:
    if sum(A) == 0:
        print("Yes")
    else:
        C = Counter(A)
        # print(C)
        if len(C) == 1 or len(C) > 3:
            print("No")
        elif len(C) == 2:
            if 0 in C and C[0] == n // 3:
                print("Yes")
            else:
                print("No")
        else:
            B = list(set(A))
            if B[0] ^ B[1] ^ B[2] == 0 and C[B[0]] == C[B[1]] == C[B[2]]:
                print("Yes")
            else:
                print("No")
