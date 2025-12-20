n = int(input())
N = [chr(97 + i) for i in range(26)]
n = n - 1
R = []
while n > 25:
    R.append(N[n % 26])
    n //= 26
    n -= 1
R.append(N[n])
print("".join(R[::-1]))
